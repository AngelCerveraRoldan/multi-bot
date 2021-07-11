import wikipedia

def summary(word):
    try:
        return wikipedia.summary(word, sentences=5)

    except wikipedia.exceptions.DisambiguationError:
        return f'There are multiple results for {word}, please be more specific.'

    except wikipedia.exceptions.PageError:
        return f'There are no wikipedia results for {word}.'
        

