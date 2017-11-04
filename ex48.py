lexicon = {
    "north": 'direction',
    "south": 'direction',
    "east": 'direction',
    "west": 'direction',
    "down": 'direction',
    "up": 'direction',
    "left": 'direction',
    "right": 'direction',
    "back": 'direction',

    "go": 'verb',
    "stop": 'verb',
    "kill": 'verb',
    "eat": 'verb',

    "the": 'stop',
    "in": 'stop',
    "of": 'stop',
    "from": 'stop',
    "at": 'stop',
    "it": 'stop',

    "door": 'noun',
    "bear": 'noun',
    "princess": 'noun',
    "cabinet": 'noun',
}

def convert_num(s):
    try:
        return int(s)
    except ValueError:
        return None


sentence = "go north east to kill a bear for the princess or 5"
def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        if convert_num(word) == None:
            word_type = lexicon.get(word) #returns value of word key
            results.append((word_type, word))
        else:
            results.append(('number', int(word)))
    return results

print(scan(sentence))
