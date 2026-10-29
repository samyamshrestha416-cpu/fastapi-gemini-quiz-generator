Quiz Generator API

A FastAPI service that creates multiple-choice quizzes on any topic using the Google Gemini API and structured output.

You send a topic and a number of questions. You get back a quiz as clean JSON: each question has four options, the position of the correct answer, and a short explanation.

This is a learning project. I built it to understand how to get reliable, validated data from an LLM instead of plain text.

How it works
The route POST /quiz receives a topic and a question count and validates them with Pydantic.
llm.py sends a prompt to Gemini and gives it a response schema: the Quiz Pydantic class. Gemini must reply in exactly that shape.
The JSON reply is turned into a Quiz object and checked by Pydantic again.
FastAPI returns the validated quiz.

The schema controls the shape of the data. The prompt controls the meaning (for example, that correct_index is the position of the right answer).

Tech stack
Python
FastAPI
Pydantic
Google Gemini API (google-genai)
python-dotenv
Project structure
quiz_generator/
├── main.py            # FastAPI app and the POST /quiz route
├── llm.py             # Gemini call that returns a Quiz object
├── schemas.py         # Pydantic classes: Question and Quiz
├── requirements.txt   # Python packages
└── .gitignore         # Keeps .env and venv out of Git
Setup
Create a virtual environment and install the packages:
bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac/Linux
   pip install -r requirements.txt
Get a Gemini API key from Google AI Studio (it has a free tier).
Create a .env file in the project folder (never upload this file):
   GEMINI_API_KEY=your_key_here
Run the server:
bash
   python -m uvicorn main:app --reload
Open http://127.0.0.1:8000/docs and try POST /quiz.

There is no database in this project.

Example

Request: POST /quiz

json
{
  "topic": "Python basics",
  "count": 2
}

Response

json
{
  "questions": [
    {
      "question": "Which keyword defines a function in Python?",
      "options": ["func", "def", "function", "lambda"],
      "correct_index": 1,
      "explanation": "Functions are defined with the def keyword."
    },
    {
      "question": "What does len([1, 2, 3]) return?",
      "options": ["2", "3", "4", "1"],
      "correct_index": 1,
      "explanation": "The list has three items."
    }
  ]
}
Validation and errors
Status	Meaning
422	Invalid input, for example count outside 1 to 10 or a very short topic
502	The AI service failed (busy, wrong key, timeout). Try again.
Known limitation

Structured output guarantees the shape of the data, not that it is correct. The model can still point correct_index at the wrong option or write a weak question, so the quiz should be reviewed before real use.

What I learned
How response_mime_type and response_schema make Gemini follow a Pydantic class
Describing nested data with a list of objects
Why the prompt still needs to explain what each field means
Limiting input (count from 1 to 10) so the API is not abused
Keeping the API key in a .env file
Ideas for improvement
A POST /quiz/score route that checks the user's answers
Hide the correct answers until the user submits
Store quizzes and scores in PostgreSQL
Difficulty levels and question types
Retry when the model returns invalid data
