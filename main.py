import requests
from datetime import datetime


TOKEN = "agtsfkdohdnsjgd"
USERNAME = "akshayalr"

app_endpoint = "https://pixe.la/v1/users"

GRAPH_ID = "codinggraph1"


user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# api_response = requests.post(url=app_endpoint, json=user_parameters)
# print(api_response.text)

graph_endpoint = f"{app_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "programming_minutes_graph",
    "unit": "minutes",
    "type": "float",
    "color": "momiji",

}

head = {
    "X-USER-TOKEN": TOKEN
}

# api_response = requests.post(url=graph_endpoint, json=graph_params, headers=head)
# print(api_response.text)

pixel_endpoint = f"{app_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date_time = datetime.now()
#print(date_time.strftime("%Y%m%d"))

pixel_params = {
    "date": date_time.strftime("%Y%m%d"),
    "quantity": "115",
}

# api_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=head)
# print(api_response)

update_pixel = f"{app_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_time.strftime('%Y%m%d')}"

update_params = {
   "quantity": "130"
}

# api_response = requests.put(url=update_pixel, json=update_params, headers=head)
# print(api_response.text)
