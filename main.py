import requests
from pprint import pprint


url = "https://akabab.github.io/superhero-api/api"
resp = requests.get(url + '/all.json')
inf = resp.json()
# pprint(inf)
heroes_list = ['Hulk', 'Captain America', 'Thanos']
summury = {}

for hero in heroes_list:
    for h in inf:
        if h['name'] == hero:
            # pprint(h['id'])
            intell = (h['powerstats']['intelligence'])
            summury[hero] = intell

pprint(summury)

print(f'Самый умный '+max(summury, key=summury.get))



# from yadisk import YaDisk
# Yandex_Token = 'y0_AgAAAABnXkMwAADLWwAAAADXyuj8CBOXgvOrQxyZv_mcmWW-QRP48Rw'
# if __name__ == '__main.py__':
#     yadisk = YaDisk(Yandex_Token)
#     yadisk.get_files_list()
