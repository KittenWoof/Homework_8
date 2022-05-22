import requests

list_names = ['Hulk', 'Captain America', 'Thanos']

def calculate_max_intelligence(names):
    max_intelligence = 0
    max_name = ""
    for name in names:
        response = requests.get('https://superheroapi.com/api/2619421814940190/search/' + name)
        for item in response.json()['results']:
            value = int(item['powerstats']['intelligence'])
            if (value > max_intelligence):
                max_intelligence = value
                max_name = name
    return [max_name, max_intelligence]

print(f"Максимальный интеллект у {calculate_max_intelligence(list_names)[0]} и он равен {calculate_max_intelligence(list_names)[1]}")