word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[:2])
print(word[2:])

# error
# word[0] = 'j'
word = 'j' + word[1:]
print(word)
n = len(word)
print(n)