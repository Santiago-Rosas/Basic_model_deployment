from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import datetime
from ms.functions import get_model_response
from basemodels.models import Input, Output


app = FastAPI()
app.title = "Churn prediction with sickit-learn"
app.version = "v0.0.1"


model_name = "SVC with Sickit-learn "
version = "v1.0.0"

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1> This is a model to predict churn, please <a href="http://localhost:8000/docs">  click here </a>  for docs </h1>')


@app.get('/info_model',tags=['Model information and services'])
async def model_info():
    """Return model information, version, how to call"""
    return {
        "name": model_name,
        "version": version
    }


@app.get('/Business',tags=['Model information and services'])
async def service():
    """Return buisness"""
    return {
        "ok"
    }


@app.post('/predict',  tags=['Model prediction'], response_model= Output)
async def model_predict(input: Input) -> Output:
    """Predict with input data as the example below"""
    response = get_model_response(input)
    return response
