


cities_in_f = {'Oslo':32, 'Bergen':26, 'Stavanger':37, 'Stord':41}

cites_in_c = {key: round((value-32) * (5/9)) for (key, value) in cities_in_f.items()}
print(cites_in_c)

weather = {'Oslo':'Raining', 'Bergen':'Thunderstorm', 'Stavanger':'Snowing', 'Stord':'Clear'}

clear_weather = {key: weather[key] for key in weather if weather[key] == 'Clear'}
print(clear_weather)

cities = {'Oslo': 32, 'Bergen': 26, 'Stavanger': 37, 'Stord': 41}
desc_cities = {key: ("WARM" if value >= 32 else "COLD") for (key, value) in cities.items()}
print(desc_cities)


def check_temp(temp):
    if temp > 33:
        return "WARM"
    elif temp < 33:
        return "COLD"
    elif temp == 33:
        return "NORMAL"

cities = {'Oslo': 32, 'Bergen': 26, 'Stavanger': 37, 'Stord': 41, 'lovund': 33}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
print(desc_cities)