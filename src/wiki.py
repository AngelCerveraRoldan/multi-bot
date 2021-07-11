import wikipedia

def summary(word):
    try:
        return wikipedia.summary(word, sentences=2, auto_suggest=False)
    
    except wikipedia.exceptions.DisambiguationError:
        return f'There are multiple results for {word}, please be more specific'

    except wikipedia.exceptions.PageError:
        return f'There are no wikipedia results for {word}.'
        
def search(word):
    try:
        return wikipedia.summary(word, sentences=10, auto_suggest=False)
    
    except wikipedia.exceptions.DisambiguationError:
        return f'There are multiple results for {word}, please be more specific'

    except wikipedia.exceptions.PageError:
        return f'There are no wikipedia results for {word}.'

def image(word, num):
    return wikipedia.page(word).images[num]
