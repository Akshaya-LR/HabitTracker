# Import the necessary modules
import requests
from datetime import datetime


# Global variables - USERNAME, TOKEN, GRAPH_ID (Name of your graph)
TOKEN = "agtsfkdohdnsjgd"
USERNAME = "akshayalr"
GRAPH_ID = "codinggraph1"

# ------------- Request Header -------------- #
head = {
    "X-USER-TOKEN": TOKEN
}

# ----------- DATE & TIME ------------- #
# Get the current date and time using datetime module
date_time = datetime.now()
# print(date_time.strftime("%Y%m%d"))


# ------------------- USER CREATION --------------- #
# PIXELA API 'user creation' - From Pixela documentation
app_endpoint = "https://pixe.la/v1/users"

# User creation parameters
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# api_response = requests.post(url=app_endpoint, json=user_parameters)
# print(api_response.text)


# -------------------- GRAPH CREATION -------------- #
# API 'Graph Creation'
graph_endpoint = f"{app_endpoint}/{USERNAME}/graphs"

# Graph creation Parameters
graph_params = {
    "id": GRAPH_ID,
    "name": "programming_minutes_graph",
    "unit": "minutes",
    "type": "float",
    "color": "momiji",

}

# api_response = requests.post(url=graph_endpoint, json=graph_params, headers=head)
# print(api_response.text)


# ----------- PIXEL CREATION ---------- #
# API 'Pixel Creation'
pixel_endpoint = f"{app_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# Pixel creation Parameters
pixel_params = {
    "date": date_time.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? "),
}

api_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=head)
print(api_response)


# -------------- UPDATE PIXEL ------------- #
# Update Pixel everyday using API and its parameters
update_pixel = f"{app_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_time.strftime('%Y%m%d')}"

update_params = {
   "quantity": "130"
}

# api_response = requests.put(url=update_pixel, json=update_params, headers=head)
# print(api_response.text)


# ---------------- DELETE PIXEL ------------ #
delete_pixel = f"{app_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_time.strftime('%Y%m%d')}"

# api_response = requests.delete(url=delete_pixel, headers=head)
# print(api_response.text)


