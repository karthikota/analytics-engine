from fastapi import FastAPI

from app.anomaly.zscore_detector import detect_anomalies
from app.dependency.dependency_mapper import generate_dependencies
from app.forecasting.cpu_forecast import forecast_cpu


app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "Analytics Engine Running"
    }


@app.get("/anomalies")
def anomalies():

    return detect_anomalies()


@app.get("/dependencies")
def dependencies():

    return generate_dependencies()


@app.get("/forecast")
def forecast():

    return forecast_cpu()