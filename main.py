import requests

locations = ['Шереметьево', 'Череповец', 'Лондон']

params = {
    'm': '',
    'n': '',
    'q': '',
    'T': '',
    'lang': 'ru'
}

for location in locations:
    url = f'https://wttr.in/{location}'
    response = requests.get(url, params=params)
    response.raise_for_status()
    print(response.text)

