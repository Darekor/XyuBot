VOWELS="аеуюоёэиы"

def transform(text):
    output = ""
    for i in text.split():
        output+=__transformWord(i)+" "
    return output

def __transformWord(word):
    firstVowelPos = __findFirstVowel(word.lower())
    return __pickStart(word,firstVowelPos)+(word[firstVowelPos+1:])

def __findFirstVowel(word):
    firstVowelPosition = -1
    for i in range(0,len(word)):
        if word[i] in VOWELS:
            firstVowelPosition=i
            break
    return firstVowelPosition

def __pickStart(word, firstVowelPos):
    FIRSTVOWEL = word[firstVowelPos]
    

    match word[firstVowelPos].lower():
        case 'а'|'я':
            start = "хуя"
        case 'у'|'ю':
            start = "хую"
        case 'и'|'ы':
            start = "хуи"
        case 'е'|'э':
            start = "хуе"
        case 'о'|'ё':
            start = "хуё"    
        case _:
            start = "хуе"
    if word[0].isupper():
        start = start.capitalize()
    return start    

    