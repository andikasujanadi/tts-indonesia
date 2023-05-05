import re

vocal = ['a','e','i','o','u','y']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def convert(sentence):
    sentence = sentence.replace(',',' , ')
    sentence = re.sub(' +',' ', sentence)
    sentence = sentence.split(' ')
    print(sentence)
    for word in sentence:
        new_word = []
        for index,letter in enumerate(word):
            if index < len(word)-3:
                if word[index] in consonant and word[index+1] in vocal and word[index+2] in consonant and word[index+3] in consonant:
                    new_word.append(word[index:index+3])
                elif word[index] in consonant and word[index+1] in vocal:
                    new_word.append(word[index:index+2])
            elif index+3 == len(word):
                if word[index] in consonant and word[index+1] in vocal and word[index+2] in consonant:
                    new_word.append(word[index:index+3])
            elif index < len(word)-1:
                if word[index] in consonant and word[index+1] in vocal:
                    new_word.append(word[index:index+2])
        print(new_word)
    return sentence

text = 'halo, nama saya rifqy, saya suka makan ayam'
convert(text)