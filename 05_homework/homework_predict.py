import requests

url = "http://<REDACTED_XXX-XXX-XXX-XXX-XXX>.compute-1.amazonaws.com:9696/predict"

# Q4
# ----------------------------------------------------------------------
# client = {"job": "student", "duration": 280, "poutcome": "failure"}
# response = requests.post(url, json=client).json()

# print(response)  # answer: {'churn_probability': 0.33480703475511053}
# ----------------------------------------------------------------------

# Q6
# ----------------------------------------------------------------------
# client = {"job": "management", "duration": 400, "poutcome": "success"}
# response = requests.post(url, json=client).json()

# print(response)  # {'churn_probability': 0.7590966516879658}