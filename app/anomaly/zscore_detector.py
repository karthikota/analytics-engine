import pandas as pd

from app.anomaly.dataframe_builder import build_dataframe


THRESHOLD = 1.0


def detect_anomalies():

    df = build_dataframe()

    if df.empty:
        print("No data available for anomaly detection.")
        return []

    cpu_mean = df["cpu"].mean()
    cpu_std = df["cpu"].std()

    anomalies = []

    for _, row in df.iterrows():

        z_score = (row["cpu"] - cpu_mean) / cpu_std

        if abs(z_score) > THRESHOLD:

            anomalies.append({
                "pod_name": row["pod_name"],
                "cpu": row["cpu"],
                "z_score": float(round(z_score, 2))
            })

    return anomalies


if __name__ == "__main__":

    results = detect_anomalies()

    print("\nANOMALIES DETECTED:\n")

    for anomaly in results:
        print(anomaly)  