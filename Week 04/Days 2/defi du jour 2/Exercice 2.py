
string = input("Input a string : ")

new_string = ""

for i in range(len(string)):
  if i == 0 or string[i] != string[i-1]:
    new_string += string[i]

print(new_string)