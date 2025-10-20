import requests

location = ['Шереметьево', 'Череповец', 'Лондон']
for i in range(len(location)):
    url = 'https://wttr.in/{}?mnqT&lang=ru'.format(location[i])
    response = requests.get(url)
    print(response.text)
