x = 1000
countries = { "Japan": 100, "Brazil": 300, "Australia": 900 }

sortedCountries = sorted(countries.items(), key=lambda item: item[1])

countriesVisited = []

for country, cost in sortedCountries:
    if x >= cost:
        countriesVisited.append(country)
        x -= cost

print(countriesVisited)
