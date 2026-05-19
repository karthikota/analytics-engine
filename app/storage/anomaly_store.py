from datetime import datetime

from app.anomaly.zscore_detector import detect_anomalies


anomaly_history = []


def store_anomalies():

    anomalies = detect_anomalies()

    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "anomalies": anomalies
    }

    anomaly_history.append(snapshot)

    return snapshot


if __name__ == "__main__":

    result = store_anomalies()

    print(result)