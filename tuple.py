
#dimentions = (500,800)
#print(dimentions[0])
#print(dimentions[1])

buffet = ("steamed_rice","fried_chicken","beef_curry","vegetable_salad","soft_drinks")

for food in buffet:
    print(food.title())
print()

buffet = ("steamed_rice","fried_chicken","bbq_chiken","vegetable_salad","oreo_shake")
for food in buffet:
    print(food.title())

print("These are the basic item provided in the every buffet party!")
print("I love buffet dineer a lot!!")


                                #in tupple you can also use the negative indexing also BOOM

id_1 = ('Elias',25,'black')
id_2 = ('Julu',26,'brown')
print(type(id_1))
id = [id_1,id_2]
print(type(id))

print()
for name,age,tone in id:
    print(name)
    print(age)
    print(tone)