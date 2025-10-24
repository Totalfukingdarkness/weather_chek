import requests

locations = ['Шереметьево', 'Череповец', 'Лондон']
payload = {'?':''}
for location in locations:
    url = 'https://wttr.in/{}?mnqT&lang=ru'.format(location)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)
