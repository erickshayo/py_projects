import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif(len(get_close_matches(word, data.keys())) > 0):
        x = input('Did you mean %s instead? Enter Y if yes, or N if no: ' % get_close_matches(word, data.keys())[0])
        if (x == 'Y'):
            return data[get_close_matches(word, data.keys())[0]]
        elif (x == 'N'):
            return 'The word does not exist. Please double check it'
        else:
            return 'We did not understand your entry.'
    else:
        return 'The word does not exist. Please double check it.'


word = input('Enter a word: ')

output = translate(word)

if (type(output)== list):
    for item in output:
        print(item)

else:
    print(output)