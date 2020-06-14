bikes = ['pulsar','cbz','hunk']                                                 #declaring a list

#for i in bikes:
 #   print(i.title())                                                           #to print all the items of a list through a loop

print()
bikes[0] = 'R15-v3'                                                             #modification of list

for i in bikes:
    print(i.title())

print()
message = "In my childhood i always dream about " + bikes[0].title() +"."      #concatation and use of title method
print(message)
print()

bikes.append("honda")
print(bikes[-1])                                                               #advance indexing of list or negative indexing

print(bikes)

del bikes[2]                                                                   #when you know the position of an element that you want to remove from a list then del function is best option
print(bikes)

bikes.remove("cbz")                                                            #to delete a specific element from list
print(bikes)

poped_item = bikes.pop()
print("The last bike that i owned is " + poped_item.title() +".")



