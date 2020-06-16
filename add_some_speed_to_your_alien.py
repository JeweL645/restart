
alien_0 = {'x-coordinates': 0, 'y-coordinates': 25, 'speed': 'medium'}
print("Original x-position: "+str(alien_0['x-coordinates']))

#alien_0['speed'] = 'fast'             #modifying the value in the dictionary
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

new_x_position = alien_0['x-coordinates'] + x_increment              #this technique is pretty cool to change the alien position
print("The new postion of the alien is "+ str(new_x_position))


