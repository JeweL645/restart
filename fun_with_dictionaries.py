friends = ['sarah', 'julu']
favourite_languages = {
    'mithso': 'c',
    'bristy': 'c++',
    'afra': 'java',
    'bornav': 'c++',
    'julu': 'python',
}
for name, fav_lan in favourite_languages.items():
    print(name.title() + "'s favorite language is: \n" + fav_lan.title())

print()

# for name in favourite_languages:
# print(name)
for name in favourite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hey " + name.title() + ",I see your favourite programming language is " + favourite_languages[
            name].title() + "!!")

if 'nabila' not in favourite_languages.keys():
    print("Nabila, you can take our poll!!")

print()
for name in sorted(favourite_languages.keys()):
    print("Thank you " + name.title() + " for taking part into the poll!!")

for language_name in set(favourite_languages.values()):
    print(language_name.title())
