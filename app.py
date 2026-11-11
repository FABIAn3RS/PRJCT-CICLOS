
import os
import requests

def fetch_data(url):
    api_key = os.environ.get("API_KEY")

    if not api_key:
        raise ValueError("La variable API_KEY no está configurada")

    response = requests.get(
        url,
        params={"key": api_key},
        timeout=10
    )

    response.raise_for_status()
    return response.json()
