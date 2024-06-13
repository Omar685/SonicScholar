import requests

data = {"user_id": 3}
response = requests.delete(f" http://127.0.0.1:3000/delete_user", json=data)
