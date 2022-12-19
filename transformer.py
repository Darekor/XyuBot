VOWELS="аеуюоёэиы"

def transform(text):
    output = ""
    for i in text.split():
        output+=__transformWord(i)
    return output

def __transformWord(word):
    return "хуе"+word