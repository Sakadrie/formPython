word=input("Entrer un caractere :")

if len(word)> 10:
    print("le mot est long")
elif len(word)<10:
    print("le mot est court")
first_carac = word[0]
last_carac = word[-1]
print("\nThe first character is ", first_carac,"\nAnd the last character is", last_carac)

wrd=""
print("Construct your string character by character :")
wdr=""
for i in word:
    wdr=wdr+i
    print(wdr)

