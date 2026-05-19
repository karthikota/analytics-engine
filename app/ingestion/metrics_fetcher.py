import requests
import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def fetch_metrics(pod_name):

    try:
        response = requests.get(
            f"{BASE_URL}/metrics/{pod_name}"
        )

        if response.status_code == 200:
            return response.json()

        else:
            print(f"API Error: {response.status_code}")
            return {}

    except Exception as e:
        print("Error fetching metrics:", e)
        return {}


if __name__ == "__main__":

    pod_name = "frontend-759775d795-rjtdf"

    metrics = fetch_metrics(pod_name)

    print(metrics)