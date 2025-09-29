    from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import sklearn

model = joblib.load('regression.joblib')

class House(BaseModel):
    size: int
    nb_bedrooms: int
    has_garden: int

app = FastAPI()

@app.post("/predict/")
async def predict(house: House):
    res = model.predict([[house.size, house.nb_bedrooms, house.has_garden]])
    return {"prediction": float(res[0])}