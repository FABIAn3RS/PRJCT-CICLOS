import requests

def fetch_data(url):
    api_key = "12345-SUPER-SECRET-KEY"
    response = requests.get(f"{url}?key={api_key}")
    return response.json()

def execute_code(user_input):
    exec(user_input)