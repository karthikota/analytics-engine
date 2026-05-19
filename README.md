# Analytics Engine

Analytics Engine for Kubernetes Observability Platform.

## Overview

This module provides:
- telemetry processing
- anomaly detection
- dependency mapping
- CPU forecasting
- analytics APIs

The engine is designed for Kubernetes/container observability systems and integrates with AI-agent and dashboard layers.

---

## Features

- Pod telemetry ingestion
- Z-score anomaly detection
- Dependency graph generation
- CPU usage forecasting
- FastAPI analytics APIs

---

## Project Structure

```text
app/
├── anomaly/
├── dependency/
├── forecasting/
├── ingestion/
├── models/
├── storage/
├── utils/
```

---

## APIs

### `/anomalies`
Returns anomaly detection results.

### `/dependencies`
Returns pod dependency relationships.

### `/forecast`
Returns predicted CPU usage.

---

## Technologies Used

- Python
- FastAPI
- Pandas
- NumPy
- Scikit-learn
- NetworkX

---

## Run Locally

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI server

```bash
uvicorn main:app --reload
```

---

## API URLs

```text
http://127.0.0.1:8000/anomalies
http://127.0.0.1:8000/dependencies
http://127.0.0.1:8000/forecast
```

---

## Notes

Current telemetry is simulated temporarily for MVP integration.

The architecture is modular and supports future integration with live Prometheus/Kubernetes telemetry.