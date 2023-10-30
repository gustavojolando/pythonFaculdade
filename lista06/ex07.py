word = input('Str: ')
word2 = input('Str2: ')

stop = False
i = 0



while not stop and i < len(word):
    if word[i] == word2:
        print(f'{word[i]} = {word2}')
        stop = True
    else:
        print(f'{word[i]}', end="")
    i += 1
