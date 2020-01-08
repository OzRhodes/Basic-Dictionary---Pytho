# very simple dictionary appl using JSON file of data
# Part of the udemy course 'The PYTHON Mega Course


import json
import os
from difflib import get_close_matches

data = json.load(open("data.json"))

def get_from_dict(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]    
    elif len(get_close_matches(word, data.keys())) > 0:
        response = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if response == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif response == "N":
            return "The word isn't in this dictionary. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word isn't in this dictionary. Please double check it."

os.system('clear')                      # clear the terminal screen
print(" A BASIC DICTIONARY\n ")
word = input("Enter word: ")            # get user input in the for of a work (str)
output = get_from_dict(word)
if type(output) == list:                # if a list is returned, pint out the options in a more readable manner
    for item in output:
        print(item)
else:
    print(output)
