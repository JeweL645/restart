aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 10, 'speed': 'slow'}
    aliens.append(new_alien)


# print(aliens)
#print("Total numbers of aliens : " + str(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 15
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = 20
        alien['speed'] = 'fast'


for alien in aliens[:5]:
    print(alien)
print("...")