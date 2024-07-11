poem_words = {}

with open("poem.txt","r") as f:
    next(f)

    for line in f:
        tokens = line.split(' ')

        for token in tokens:
            token = token.replace('\n', '')

            if token in poem_words:
                poem_words[token] += 1

            else:
                poem_words[token] = 1


print(poem_words)




