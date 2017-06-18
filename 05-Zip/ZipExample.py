countries = ['India','USA','China','UK','Australia']

gold = [12,50,100,35,40]
silver = [34,66,75,45,41]
bronze = [45,78,89,55,43]

medals = list(zip(countries,gold,silver,bronze))
print(medals)

# Only gold with countries
countries_with_gold = list(zip(countries,gold))
print(countries_with_gold)

for i in range(len(countries)):
    c = countries[i]
    g = gold[i]
    s = silver[i]
    b = bronze[i]

    print(c, g+s+b)