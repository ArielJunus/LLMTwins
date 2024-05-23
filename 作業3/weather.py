import requests

##this part weather.py uses weather api key to get data for a specific area and put it into the server

def get_weather_from_opendata(url, api_key, location=None):
  parameters = f'?appid={api_key}&q={location}&units=metric'
  full_url = url + parameters
  
  try:
    response = requests.get(full_url)
    response.raise_for_status()

    data = response.json()
    
    return {
      'location': data['name'],
      'temperature': data['main']['temp'],
      'humidity': data['main']['humidity'],
    }
  except requests.exceptions.RequestException as e:
    print('Error retrieving weather data: ', e)

def set_device_status(status):
  url = 'http://127.0.0.1:5000'
  path = '/device/status'
  api_key = 'ZV57oAEStAZltOBBW4NtaC6QdSDPCdG1'

  headers = {
    'Content-Type': 'application/json',
    'Api-Key': api_key
  }
  payload = {
    'status': status
  }
  return requests.post(url + path, headers=headers, json=payload)

url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = '8f54f89d3afb9bf113bef482107e8c7f'

while True:
  location = str(input('Temperature in: '))

  response = get_weather_from_opendata(url, api_key, location)
  print(response)

  set_device_status(response)