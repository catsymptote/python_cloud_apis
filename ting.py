import requests
import json



LONGITUDE = 60.8
LATITUDE = 10.7
API_LINK = f'https://www.7timer.info/bin/astro.php?lon={LONGITUDE}&lat={LATITUDE}&ac=0&unit=metric&output=json&tzshift=0'
# API_LINK = 'https://api.7timer.info/bin/astro.php?lon=' + str(LONGITUDE) + '&lat=' + str(LATITUDE) + '&ac=0&unit=metric&output=json&tzshift=0'
# API_LINK = 'https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0'


response = requests.get(API_LINK)

data = response.json()
# print(data['dataseries'][0])


with open('data_ting.json', 'w') as outfile:
    outfile.write(json.dumps(data, indent=4))
