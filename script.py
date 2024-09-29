import requests

def fetch_jokes():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    data = response.json()
    print(data['setup'] + " : " + data['punchline'])

fetch_jokes()