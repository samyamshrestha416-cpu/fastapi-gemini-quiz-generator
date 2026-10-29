from pydantic import BaseModel, Field

class Question(BaseModel):
    question : str
    options : list[str]
    correct_index : int
    explanation : str

class Quiz(BaseModel):
    questions : list[Question]

# print(Quiz(questions=[Question(question="2+2?", options=["3","4","5","6"], correct_index=1, explanation="Basic math")]))

