from fastapi import FastAPI,Path
from sentianalysis import get_me_my_result
from pydantic import BaseModel
app = FastAPI()

class Phrase(BaseModel): 
    text: str

@app.post("/get-sentiments/")
def get_sentiments(script: Phrase):
    print(f'{script.text}')
    sentiments = get_me_my_result(script.text)
    if sentiments["compound"] <= -0.4:
        return {"status" : "Success", "sentiment" : "Negative"}
    elif sentiments["compound"] >= 0.5:
        return {"status" : "Success", "sentiment" : "Positive"}
    else:
        return {"status" : "Success", "sentiment" : "Neutral"}
