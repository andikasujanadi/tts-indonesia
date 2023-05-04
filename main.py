vocal = ['a','e','i','o','u']
consonant = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def convert(sentence):
    sentence = sentence.split(' ')
    for word in sentence:
        new_word = []
        for index,letter in enumerate(word):
            if index > 0 and index < len(word):
                if word[index-1] in consonant and word[index] in vocal:
                    new_word.append(word[index-1:index+1])
        print(new_word)
    return sentence

text = 'halo, nama saya rifqy, saya suka makan ayam'


print(convert(text))