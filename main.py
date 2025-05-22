from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from llm_local import process_text

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("LOCAL_API_KEY")

class InputText(BaseModel):
    text: str
    task: str = "generate"

@app.post("/llm")
def llm_endpoint(data: InputText, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        result = process_text(data.text, data.task)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
