from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import joblib
import pandas as pd
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


pipeline = joblib.load("ogrenci_basari_modeli.pkl")


class StudentFeatures(BaseModel):
    age: float
    gender: str
    study_hours_per_day: float
    social_media_hours: float
    netflix_hours: float
    sleep_hours: float
    attendance_percentage: float
    exercise_frequency: float
    mental_health_rating: float
    part_time_job: str
    diet_quality: str
    internet_quality: str
    parental_education_level: str
    extracurricular_participation: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(features: StudentFeatures):

    input_data = pd.DataFrame([features.model_dump()])
    
    
    prediction = pipeline.predict(input_data)
    
    return {"predicted_score": float(prediction[0])}