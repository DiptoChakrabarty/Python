#def is_vowel(letter):
 #   return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    l=['a', 'e', 'i', 'o', 'u', 'y']
    
    #words=words.split(" ")
    n=len(words)
    for i in range(n):
        num_vowels = 0
        p=words[i]
        for j in len(p):
            if j in l:
                num_vowels += 1
        if num_vowels % 2 == 0:
            score = score+2
        else:
            score=score+1
    return score
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    #t=len(words)
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score = score+2
        else:
            score=score+1
    return score
