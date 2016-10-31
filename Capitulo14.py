import json

import sys

if len(sys.argv) < 2:
    print('Usage: script.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

url = 'http://openweathermap.org/city/3445831' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
w = weatherData['list']
print('Clima atual e %s:' % (location))
print(w[0]['clima'][0]['main'], '-', w[0]['clima '][0]['descricao'])
print()
print('Amanha:')
print(w[1]['clima'][0]['main'], '-', w[1]['clima'][0]['descricao'])
print()
print('Depois de amanha:')
print(w[2]['clima'][0]['main'], '-', w[2]['clima'][0]['descricao'])
