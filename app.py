import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def findWord(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        s_word = get_close_matches(word, data.keys())[0]
        c = input("Did you mean %s ? Y for yes N for no: " % s_word)
        if(c == "Y" or c == "y"):
            return data[s_word]
        else:
            return "Word does not exist"
    else:
        return "Word does not exist"


word = str(input("Enter a word: "))

word = word.lower()

output = findWord(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
