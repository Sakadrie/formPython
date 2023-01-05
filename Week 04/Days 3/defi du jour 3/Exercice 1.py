
word = input("Input a word : ")

letters = {}

for i, letter in enumerate(word):
  if letter not in letters:
    letters[letter] = []
  letters[letter].append(i)

print(letters)