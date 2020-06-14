
users = ['julu','admin']

if users:
    print()
else:
    print("We need to find some users! ")

for user in users:
    if user == 'admin':
        print("Hello "+user.title()+" :) Do you want to see the status?")
    else:
        print("Hello " + user.title() + ". thank you for logging again!")


