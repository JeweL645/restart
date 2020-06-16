favourite_languages = {
    'mithso': 'c',
    'bristy': 'c++',
    'afra': 'java',
    'bornav': 'c++',
    'julu': 'python',
}

friends = ['sarah','bornav','tonni','afra','mustahid','julu','amit','omer']

for people in friends:
    if people in favourite_languages.keys():
        print("Thank you "+people.title()+" for taking part into the poll!!")
    else:
        print(people.title()+ " you should take part to the polling!")