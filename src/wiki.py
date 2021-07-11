import wikipedia

def summary(word):
    print(wikipedia.summary(word))

def content(word):
    print(wikipedia.page(word).content)
