import requests
from data import config
from icecream import ic


url = config.GOOGLE_URL.format(GOOGLE_API=config.GOOGLE_API)

response = requests.get(url)
data = response.json()
print(response.text)
ic(data)
