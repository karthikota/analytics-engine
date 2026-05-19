import requests
import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def fetch_pods():

    try:
        print(BASE_URL)
        print(f"{BASE_URL}/pods")
        response = requests.get(f"{BASE_URL}/pods")

        if response.status_code == 200:
            return response.json()

        else:
            print(f"API Error: {response.status_code}")
            return []

    except Exception as e:
        print("Error fetching pods:", e)
        return []


if __name__ == "__main__":

    pods = fetch_pods()

    application_pods = [
        pod for pod in pods
        if pod["namespace"] == "default"
    ]

    print("\nAPPLICATION PODS:\n")

    for pod in application_pods:
        print(pod["name"])