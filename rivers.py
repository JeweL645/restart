
rivers = {
    'bangladesh': 'padma',
    'india': 'ganga',
    'egypt': 'nile',
}
for country, r_name in rivers.items():
    print(r_name.title()+" runs through in "+country.title())

print()

print("Name of the rivers in the following: ")
for river in rivers.values():
    print(river.title())

print()
print("Name of the countries in the following: ")
for country in rivers.keys():
    print(country.title())
