import json
from difflib import get_close_matches

data = json.load(open("15)_P_English Dictionary\data.json")) # data becomes automatically a dictionary

def translate(w):
    w = w.lower() # Converting to lowercase to match the key of the dictionary

    # rain.....Exact word
    if w in data:
        return data[w]

    # Delhi...To identify places that start with Caps
    elif w.title() in data:
        return data[w.title()]

    # NASA...To identify acronyms
    elif w.upper() in data:
        return data[w.upper()]

    # rainn.... To get closely matching words
    elif len(get_close_matches(w, data.keys()))>0:
        res = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0]) # get_close_matches gives out a list of similar words to the word entered...we extract the 1st word in the list
        if res == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif res == "N":
            return "Word doesn't exist!"
        else:
            return "We didn't understand your entry"

    # ofwwenunw...Random word
    else:
        return "Word doesn't exist!"


word = input("Enter word : ")
output = translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output) # This is incase the o/p is a string