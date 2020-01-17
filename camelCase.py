sentence = input('Please write a sentence ')
words = sentence.split(" ")

# specific solution in credit to: https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension#4260304
changedWords = [word.title() if words.index(word)!=0 else word.lower() for word in words]
camelCat = ''

for word in changedWords:
    camelCat+=word
print(camelCat)