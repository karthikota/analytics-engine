import requests
import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

response = requests.get(f"{BASE_URL}/pods")

print("STATUS CODE:", response.status_code)
print("RAW RESPONSE:")
print(response.text)