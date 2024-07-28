import requests
from requests.auth import HTTPBasicAuth

username = "anadmin123"
password = "admin123"

# Define the URL of the FastAPI server
url = f"http://127.0.0.1:8000/name/{username}"  # Replace "your_name" with the actual name you want to use

# Make the GET request with Basic Authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check the response status code
if response.status_code == 200:
    # Print the JSON response
    print(response.json())
else:
    print(f"Failed to authenticate: {response.status_code}")
