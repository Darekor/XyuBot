VOWELS="аеуюоёэиы"

def transform(text):
    output = ""
    for i in text.split():
        output+=__transformWord(i)+" "
    return output

def __transformWord(word):
    firstVowelPos = __findFirstVowel(word)
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
            return "хуя"
        case 'у'|'ю':
            return "хую"
        case 'и'|'ы':
            return "хуи"
        case 'е'|'э':
            return "хуе"
        case 'о'|'ё':
            return "хуё"    
        case _:
            return "хуе"
    

    