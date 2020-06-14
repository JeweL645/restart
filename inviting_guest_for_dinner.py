number_of_guest = input('Enter the number of guest: ')
n = int(number_of_guest)

guest_list = []

for i in range(n):
    name = input('Enter the guest name: ')
    guest_list.insert(i,name)

#I = i
#print(I)

for j in guest_list:
    print(j.title() +" Dst amar bashay tor dawat" + "!")

print()

pop_friend = guest_list.pop(0)
print("Tui keno ashte parbi na "+ pop_friend.title() + "?")

print()

guest_list.insert(0, "bristy".title())
for j in guest_list:
    print(j.title() +" Dst amar bashay tor dawat" + "!")
print()

print("Yahoo! I've found a bigger dinner table, I can manage for everyone!! ")
print()

guest_list.insert(i+1, 'afra')
guest_list.insert(i+2, 'jitu')
guest_list.append('shuvo')

for j in guest_list:
    print(j.title() +" Dst amar bashay tor dawat" + "!")
print()

num = len(guest_list)
msgg = "I need to arrange for " + str(num) + " people"
print(msgg)

print("Guys I'm really sorry!")
print()

s1 = guest_list.pop()
print(s1.title() + " Sorry dst, I can't make it this time")

s2 = guest_list.pop()
print(s2.title() + " Sorry dst, I can't make it this time")

s3 = guest_list.pop()
print(s3.title() + " Sorry dst, I can't make it this time")

s4 = guest_list.pop()
print(s4.title() + " You are in Best friend!")

s5 = guest_list.pop()
print(s5.title() + " Man you are in!")

s6 = guest_list.pop()
print(s6.title() + " Sorry dst, I can't make it this time")

print(guest_list)
print("yes!!")