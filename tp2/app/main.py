from contextlib import asynccontextmanager
import random

import mlflow
from fastapi import FastAPI
from pydantic import BaseModel

MLFLOW_TRACKING_URI = "http://localhost:5000"
MLFLOW_MODEL_NAME = "IrisModel"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.sklearn.autolog()

current_model = None
next_model = None
p = 0.1


class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class UpdateRequest(BaseModel):
    version: str


def load_model(version: str = 'latest'):
    model_uri = f"models:/{MLFLOW_MODEL_NAME}/{version}"
    return mlflow.sklearn.load_model(model_uri)


@asynccontextmanager
async def lifespan(app: FastAPI):
    global current_model, next_model
    current_model = load_model()
    next_model = load_model()
    print("Model Chargé")
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/predict")
async def predict(iris: Iris):
    print(iris)
    data = [[
        iris.sepal_length,
        iris.sepal_width,
        iris.petal_length,
        iris.petal_width
    ]]

    if random.random() < p:
        model = next_model
    else:
        model = current_model

    return {"prediction": float(model.predict(data)[0])}


@app.post("/update-model")
async def update_model(req: UpdateRequest):
    global next_model
    next_model = load_model(req.version)
    return {"status": "OK"}


@app.post("/accept-next-model")
async def accept_next_model():
    global current_model
    current_model = next_model
    return {"status": "OK"}