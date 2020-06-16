# A simple dictionary
#A dictionary is a key value pairs
Color = input("Enter the color: ")
Points = int(input("Enter the points: "))

alien_0 = {'color': Color, 'points': Points}            #you need to use the curly braces to specify a dictionary

print(alien_0['color'])                            # you need to print an element like nameOfTheDict[theParticularElement]
print(alien_0['points'])

alien_0 = {'color': Color, 'points':Points}            #here color and points are keys
                                                   #red and 15 are values
                                                   #now these value can be string, list, number even anther dictionaries

    #Accessing values in a dictionaries
new_points = alien_0['points']
print("You just earned "+ str(new_points) +" points  right now!")
