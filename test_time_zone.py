import requests

from icecream import ic

url = 'https://www.timeapi.io/api/Time/current/zone?timeZone=Poland/Gdanks'
response = requests.get(url)
data = response.json()
# time = data['time']
ic(data)
