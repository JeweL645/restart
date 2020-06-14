
fav_food = ["pizza","pasta","bbq_rice","nachos","milk_shakes","ice_cream"]
#print(fav_food)
for food in fav_food:
    print(food.title()+"!!")

print("First three items in the list are:\n")

for food in fav_food[:3]:
    print(food.title())


print("The three item in the middle of the list are :")
for food in fav_food[2:5]:
    print(food.title())

print("The three item in the last of the list are :")
for food in fav_food[3:]:
    print(food.title())