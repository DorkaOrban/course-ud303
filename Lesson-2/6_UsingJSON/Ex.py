a = requests.get('http://swapi.co/api/people/1/')
print(a.json()['name'])