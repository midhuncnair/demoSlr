# https://blog.finxter.com/deploying-a-machine-learning-model-in-fastapi/

import pickle

import uvicorn
import numpy as np

from fastapi import FastAPI

from .constants import MODEL_PICKLE_FILE_NAME


app = FastAPI()


pickle_in = open(MODEL_PICKLE_FILE_NAME, "rb")
model = pickle.load(pickle_in)


@app.get("/")
async def root():
   return {"message": "Hello World"}


@app.post("/predict")
def predict(X:float):
   data = np.array([[X]])
   prediction = model.predict(data)
   return {
       'prediction': prediction[0],
   }
