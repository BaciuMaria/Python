# Problema 1
# Find The greatest common divisor of multiple numbers read from the console.
numere = int(input("Cate numere vrei sa introduci: "))
while numere < 2 : numere = int(input( "Introduceti un numar mai mare sau egal cu 2 : "))

cmmdc= int(input())

for i in range(1,numere):
    n = int(input())
    x = cmmdc
    y = n
    while y != 0:
      z = x % y
      x = y
      y = z
    cmmdc = x

print(f"Cel mai mare divizor comun: {cmmdc}")

# Problema 2
# Write a script that calculates how many vowels are in a string.

string = input("Introduceti un sir de caractere : ")
nr_vocale = 0

for caracter in string :
    if caracter in 'aeiou':
        nr_vocale = nr_vocale + 1

print(f"Cuvantul contine {nr_vocale} vocale.")

# Problema 3
# Write a script that receives two strings and prints the number of occurrences of the first string in the second.

string1 = input("Introduceti primul sir : ")
string2 = input("Introduceti al doilea sir : ")

nr_apariti = string1.count(string2)

print(f"Al doilea sir apare de {nr_apariti} ori in primul sir.")

# Problema 4
# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

string = "ImiFacTemaLaPython"
final_string = string[0].lower()

for caracter in string[1:] :
    if caracter.isupper() :
        final_string = final_string + "_" + caracter.lower()
    else :
        final_string = final_string + caracter

print(f"{string} --> {final_string}")

# Problema 6
# Write a function that validates if a number is a palindrome.

numar = int(input("Introdu un numar :"))
nr_initial = numar
oglindit = 0
while numar > 0 :
    cifra = numar % 10
    oglindit = oglindit*10 + cifra
    numar = numar//10
if nr_initial == oglindit :
    print(f"{nr_initial} este palindrom.")
else : print(f"{nr_initial} nu este palindrom.")
