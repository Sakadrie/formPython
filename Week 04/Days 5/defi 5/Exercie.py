# Instructs the user to enter a sequence of words separated by commas
words = input("Saisissez une séquence de mots séparés par des virgules : ")

# Separates the word string into a word list
words_list = [word.strip() for word in words.split(',')]

#  Sorts the word list alphabetically
words_list.sort()

# Displays the comma-separated list of words
print(', '.join(words_list))