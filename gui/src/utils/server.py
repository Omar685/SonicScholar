import requests

def check_server_work(url: str):
  try:
    response = requests.get(url, timeout=1)
    if response.status_code >= 200 and response.status_code <300: return True
    else: return False
  except requests.exceptions.RequestException as e:
    return False



URL = "http://127.0.0.1:3000"
if check_server_work(URL):
  print(True)
else:  
  print(False)