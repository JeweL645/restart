pizzas = ["extracheese","nagamixed","pepperoni","redchilli"]
fav_pizza ='hot'
for pizza in pizzas:
    print("I like "+pizza.title()+" pizza!!\n")

print("Besides beef masala is love!")
print("Or the BBQ chicken is something else for me!")
print("Or you can add to my fav list club pizza as well!")
print("Dude basically I love pizza a lot being very honest!")

friend_pizzas = pizzas[:]
friend_pizzas.append("bbq")

print("\nMy favourite pizzas are: ")
for piz in pizzas:
    print(piz.title())

print("\nMy friends favourite pizzas are: ")
for pizz in friend_pizzas:
    print(pizz.title())

print('extracheese' in pizzas)
print("i'm here")
if fav_pizza not in pizzas:
    print("There's no pizza called " + fav_pizza +" in the list! ")

