import os
from dotenv import load_dotenv
from google import genai
import json
from google.genai import types
from schemas import Quiz

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def generate_quiz(topic: str, count: int) -> Quiz:
    prompt = f"""Create {count} multiple-choice questions about {topic}.
Each question has exactly 4 options.
correct_index is the position (0 to 3) of the right answer.
Add a short explanation for each answer."""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Quiz,
        ),
    )
    return Quiz(**json.loads(response.text))

# if __name__ == "__main__":
#     quiz = generate_quiz("Python basics", 3)
#     for q in quiz.questions:
#         print(q.question)
#         print(q.options)
#         print("Answer:", q.options[q.correct_index])
#         print()