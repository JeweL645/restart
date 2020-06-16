favourite_languages = {
    'mithila': ['c'],
    'bristy': ['c++', 'ruby'],
    'bornav': ['larabel', 'r'],
    'afra': ['c', 'java', 'php'],
    'julu': ['python', 'c'],
}

for name, languages in favourite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favourite languages are:\t")
        for language in languages:
            print(language.title())
    else:
        print("\n" + name.title() + "'s favourite language is:\t")
        for language in languages:
            print(language.title())
