## Return the the first word and the rest of the sentence all in lowe case
def change(sentence):
    sentence = sentence.split()

    word = sentence[0]
    rest = ' '.join(sentence[1:])
    
    return word, rest

