
current_users = ['julu', 'samiul', 'chobi', 'mithso', 'barish', 'lots', 'toto', 'shuvo', 'admin']
#print(current_users)
#for current_user in current_users:
    #print(current_user.title())

new_users = ['julu', 'samiul', 'yeasin', 'chobi', 'nusraat', 'parisa', 'zara', 'farzeen']

for new_user in new_users:
    if new_user in current_users:
        print(new_user)
        print("This "+new_user.title()+" is unavailable,"+" You need to input new username as it has been taken already! ")
    else:
        print("The username is available "+ new_user.title())


