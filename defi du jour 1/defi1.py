word=input("Entrer un caractere :")

if len(word)> 10:
    print("le mot est long")
elif len(word)<10:
    print("le mot est court")
wdr=""
for i in word:
    wdr=wdr+i
    print(wdr)

