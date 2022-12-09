## Exercice 1
my_fav_numbers= ['1','2']

friend_fav_numbers= ['10','12']

my_fav_numbers.append('3')
my_fav_numbers.append('4')

our_fav_numbers = friend_fav_numbers + my_fav_numbers

print(my_fav_numbers)
del my_fav_numbers[3]
print(my_fav_numbers)
print(our_fav_numbers)

print("\n\n")
####Exercice 2
print("il n'est pas possible de modifier un tuple donc on pourrait pas ajouter a un tuple deja cree")
print("\n\n")
###Exercice 3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
print(basket)
basket.remove('Blueberries')
print(basket)
basket.append('kiwi')
print(basket)
basket.insert(0,'Apples')
print(basket)
basket.insert(0,'Apples')
print(basket)
basket.insert(0,'Apples')
print(basket)
print("\n\n")

###Exercice 4
print("un entier est un nombre sans virugule qui comporte l'ensemble (0,1,2,3,4,5,6,7,8,9) ")
## 
print("un float est un nombre a virgule comportant l'ensemble des nombres decimal")
flottant=['1.5','2','2.5']
print(flottant)

print("\n\n")
#Exercice 5

for i in range(21):
    print(i)
for i in range(21):
    if i%3:
        print(i)

print("\n\n")
##Exercice 6
name=""
while name != "Adrie":
    name=input("Entrer votre nom:")

print("\n\n")
## Exercice 7
""" Exercise 7 : FAVORITE FRUITS """
fruits = input('Enter your favorite(s) fruits (NB: Separate fruit with a single space): ')
fruits_list  = list()
fruits_list = fruits.split()

my_fruits = input('Enter a fruit name : ')
test = 0
for i in fruits_list:
    if my_fruits == i:
        test = 1

if test == 1 :
    print("You have choose one of your favorite fruits, great !!")
else :
    print("This fruit is not one of your favorite fruits")          

###Exercice 8
""" Exercise 8: WHO ORDERED A PIZZA ?"""
L = list()
p = 0
while True:
    pizzas = input('Enter a pizza(s) topping (or tape quit to cancel): ')
    if pizzas != 'quit':
        L.append(pizzas)
        print("You add {} to the pizza\'s topping list ".format(pizzas))
        p = p + 2.5
    else:
        pizzas = ""
        break    
print("All topping : ", L, "\n", "The total price of this pizza with all topping are :", 10+p)

## Exercice 9

""" Exercise 9 : CINEMAX"""
P=0      # price initialization
nb=int(input("Hello!! How many are you?"))  # family's numbers initialization

# Cost to pay according to the age of the family's members
for i in range(0,nb):

    age=int(input("Enter your person's age: "))
    print("Next person!")
    if age<3:
        # free ticket
        P=P+0
        
    elif 3<age<=12:
        # ticket's price is 10
        P=P+10
        
    elif age>12:
        # ticket's price is 15
        P=P+15    
 
    
print("For all (",nb,") member(s), amount is ",P)



P=0      # price initialization
nb=int(input("Hello! How many are you? : "))  # family's numbers initialization
Name=[]     # list of saved's name
k=nb
#Cost to pay according to the age of the family's members
for i in range(0,nb):
    name=input("Enter your name: ")
    age=int(input("Enter your age : "))
    Name.append(name)
    print("Saved... Pass to the next person")
    
    
    # check age

    if 16<=age<=21:
        # ticket's price is 10
        P=P+10
    else:
        # free ticket
        print("You are not allowed to watch this movie")
        k=k-1
        
        Name.remove(name) # delete the name
           
print(Name)    
print("For all (",k,") member(s), amount is ",P)

# Exercice 10
"""Exercise 10: SANDWICH ORDERS"""
# List of sandwich
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# creation of empty list
finished_sandwiches = list()
# create "p" which will allow us to determine the exact number of sandwiches prepared
p = 0
# remove ready-made sandwiches
while sandwich_orders !=[]:
    test =input("What sandwich did you finish making?")
    if test in sandwich_orders:
        sandwich_orders.remove(test)
        finished_sandwiches.append(test)
        p = p + 1

# Print the ready-made sandwiches
for i in range(0, p):
    print("I made your",finished_sandwiches[i])
    
# Exercice 11
""" Exercise 11 : SANDWICH ORDERS 2"""

sandwich_orders = ["Pastrami sandwich", "Tuna sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = list()
p = 0
print("ALERT!!! Charcuterie no longer has pastrami")


# pastramis delete
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

while sandwich_orders != [] :
    test = input("What sandwich did you finish making? ")
    if test in sandwich_orders:
        sandwich_orders.remove(test)
        finished_sandwiches.append(test)
        p = p + 1

# print the finished sandwich without pastramis
for i in range(0, p):
    print("I made your",finished_sandwiches[i])
