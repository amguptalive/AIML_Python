import os

import requests
from datetime import datetime

APP_ID = os.environ.get('ENV_NIX_APP_ID')
APP_KEY = os.environ.get('ENV_NIX_APP_KEY')
TOKEN = os.environ.get('ENV_SHEETY_TOKEN')
SHEET_ENDPOINT = os.environ.get('ENV_SHEETY_ENDPOINT')
nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

exercise_params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 172,
    "age": 43,
}
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

response = requests.post(url=nutrition_endpoint, json=exercise_params, headers=headers)
result = response.json()
################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheet_headers = {
    "Authorization": TOKEN
}
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=sheet_headers)

    print(sheet_response.text)
