num = int(input("Entrer un number : "))
print("\n")
leng = int(input("Entrer un lenght : "))

dico = []

for x in range (1, leng+1):
    dico.append(num*x) 
print(dico)