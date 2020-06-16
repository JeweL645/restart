# storing information of a pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese', 'red chilli sauce'],
}

print("You ordered a "+pizza['crust'].title()+"-crust pizza"+" with the following toopings: ")
for tooping in pizza['toppings']:
    print(tooping.title())

