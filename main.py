from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from schemas import Quiz
import llm

app = FastAPI()

class QuizRequest(BaseModel):
    topic : str = Field(min_length=2)
    count : int =Field(ge=1 ,le=10)

@app.post("/quiz",response_model=Quiz)
def Quiz_qns(request: QuizRequest):
    try:
        result =llm.generate_quiz(request.topic,  request.count)
    except Exception:
        raise HTTPException(status_code=502, detail="The AI service failed, try again")
    return result