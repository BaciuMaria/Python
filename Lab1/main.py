# Problema 1
# Find The greatest common divisor of multiple numbers read from the console.
numere = int(input("1.) Cate numere vrei sa introduci: "))
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

string = input("2.) Introduceti un sir de caractere : ")
nr_vocale = 0

for caracter in string :
    if caracter in 'aeiou':
        nr_vocale = nr_vocale + 1

print(f"Cuvantul contine {nr_vocale} vocale.")

# Problema 3
# Write a script that receives two strings and prints the number of occurrences of the first string in the second.

string1 = input("3.) Introduceti primul sir : ")
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

print(f"4.) {string} --> {final_string}")

# Problema 6
# Write a function that validates if a number is a palindrome.

numar = int(input("6.) Introduceti un numar :"))
nr_initial = numar
oglindit = 0
while numar > 0 :
    cifra = numar % 10
    oglindit = oglindit*10 + cifra
    numar = numar//10
if nr_initial == oglindit :
    print(f"{nr_initial} este palindrom.")
else : print(f"{nr_initial} nu este palindrom.")

# Problema 7
# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD",
# this function will return 123, or if the text is "abc123abc" the function will extract 123).
# The function will extract only the first number that is found.

def primul_numar(string):
    index = -1
    primul_nr = ""
    for i,caracter in enumerate(string):
        if caracter.isdigit() :
            index = i
            break

    while string[index].isdigit():
        primul_nr = primul_nr + string[index]
        index = index + 1


    if primul_nr:
        return int(primul_nr)
    else : return None

string = input("7.) Introduceti un sir de caractere:")
numar = primul_numar(string)
print(f"Primul numar din sir : {numar}")

# Problema 8
# Write a function that counts how many bits with value 1 a number has.
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

def count_1(numar):

    count = 0
    binar = bin(numar).replace("0b","")
    for bit in binar :
       if bit == '1' :
           count = count + 1
    return count

numar = int(input("8.) Introduceti un numar: "))
count = count_1(numar)
print(f"Numar {numar} contine {count} biti de valoare 1.")

# Problema 10
# Write a function that counts how many words exists in a text.
# A text is considered to be form out of words that are separated by only ONE space.
# For example: "I have Python exam" has 4 words.

def numar_cuvinte(string):
    cuvinte = string.split()
    return len(cuvinte)

string = input("10.) Introduceti un text: ")
numar = numar_cuvinte(string)
print(f"Textul contine {numar} cuvinte.")
