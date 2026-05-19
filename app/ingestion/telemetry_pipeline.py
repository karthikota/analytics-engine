from app.ingestion.pod_fetcher import fetch_pods
from app.utils.sample_metrics import generate_sample_metrics


def build_telemetry():

    pods = [
    {"name": "frontend", "namespace": "default"},
    {"name": "paymentservice", "namespace": "default"},
    {"name": "checkoutservice", "namespace": "default"},
    {"name": "recommendationservice", "namespace": "default"}
            ]
    

    application_pods = [
        pod for pod in pods
        if pod["namespace"] == "default"
    ]

    telemetry = []

    for pod in application_pods:

        pod_name = pod["name"]

        metrics = generate_sample_metrics(pod_name)

        telemetry.append(metrics)

    return telemetry


if __name__ == "__main__":

    data = build_telemetry()

    for item in data:
        print(item)