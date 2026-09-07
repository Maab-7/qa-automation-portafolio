import os
import requests
from dotenv import load_dotenv
from pathlib import Path

# Explicitly find .env file in the project root directory
load_dotenv(dotenv_path=Path(__file__).parent.parent / '.env')

BASE_URL = "https://reqres.in/api"
API_KEY = os.getenv("REQRES_API_KEY")

HEADERS = {
    "x-api-key": API_KEY
}


def _build_url(endpoint):
    clean_endpoint = endpoint.lstrip("/")
    return f"{BASE_URL}/{clean_endpoint}"


def get(endpoint, params=None):
    return requests.get(_build_url(endpoint), headers=HEADERS, params=params)


def post(endpoint, payload):
    return requests.post(_build_url(endpoint), headers=HEADERS, json=payload)


def put(endpoint, payload):
    return requests.put(_build_url(endpoint), headers=HEADERS, json=payload)


def delete(endpoint):
    return requests.delete(_build_url(endpoint), headers=HEADERS)



