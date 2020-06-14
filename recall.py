#a program for countries

country = ['bangladesh','india','srilanka','nepal','vutan']
print(country)
country.insert(6, 'indoneshia')
country.append('china')
del country[1]
country.pop()
country.pop(3)

l = len(country)
print(l)
print()

for i in country:
    print(i.title())

print(sorted(country))
print(country)

country.sort()
print(country)

country.sort(reverse=True)
print(country)

country.reverse()
print(country)

country.reverse()
print(country)

country.remove('nepal')
print(country)

country[0] = 'new-zeeland'
print(country)

