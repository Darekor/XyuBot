VOWELS="аеуюоёэиы"

def transform(text):
    output = ""
    for i in text.split():
        output+=__transformWord(i)
    return output

def __transformWord(word):
    cutOff = __findFirstVowel(word)+1
    return "хуе"+(word[cutOff:])

def __findFirstVowel(word):
    firstVowelPosition = -1
    for i in range(0,len(word)):
        if word[i] in VOWELS:
            firstVowelPosition=i
            break
    return firstVowelPosition