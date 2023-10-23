# Problema 1
# Write a function to return a list of the first n numbers in the Fibonacci string.

def fib_n_numere(n):
   lista = []
   x = 0
   y = 1
   z = 1

   for _ in range(n):
      lista.append(x)
      x = y
      y = z
      z = x + y

   return lista

n = int(input("1.) Introduceti un numar: "))
rezultat = fib_n_numere(n)
print(f"Primele {n} numere din sirul lui Fibonacci : {rezultat}")

# Problema 2
# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

numere = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def cauta_nr_prime(lista):
   lista_prime= []
   for i in lista:
      if este_prim(i):
         lista_prime.append(i)
   return lista_prime

def este_prim(n):
   if n == 1:
      return False
   elif n > 1:
      for i in range (2,n):
         if n % i == 0:
            return False
   return True

nr_prime = cauta_nr_prime(numere)
print(f"2.) {numere}")
print(f"Lista numerelor prime: {nr_prime}")

# Problema 3
# Write a function that receives as parameters two lists a and b and returns:
# (a intersected with b, a reunited with b, a - b, b - a)

a = [1,3,4,5,8,9,10]
b = [2,4,5,6,7,8]

print(f"3.) Lista a: {a}")
print(f"Lista b: {b}")

def operatii_liste(a, b):
   intersectie = list(set(a) & set(b))
   reuniunea = list(set(a) | set(b))
   diferenta_a_b = list(set(a) - set(b))
   diferenta_b_a = list(set(b) - set(a))
   return intersectie,reuniunea,diferenta_a_b, diferenta_b_a

rezultat = operatii_liste(a,b)
print(f"Intersectia lui a si b: {rezultat[0]}")
print(f"Reuniunea lui a si b: {rezultat[1]}")
print(f"a - b : {rezultat[2]}")
print(f"b - a : {rezultat[3]}")

# Problema 4

def compose(note_muzicale, poziti , poz_curenta):
   melodie = []
   melodie.append(note_muzicale[poz_curenta])
   for poz in poziti :
      poz_curenta = (poz_curenta + poz) % len(note_muzicale)
      melodie.append(note_muzicale[poz_curenta])
   return melodie

rezultat = compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
print(f"4.) {rezultat}")

# Problema 5
m = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]
print(f"5.) Matricea : ")
for row in m:
    print(row)

def zero_sub_diag_principala(matrice):
   for i in range(len(matrice)):
       for j in range(0,i):
           matrice[i][j] = 0
   return matrice

rezultat = zero_sub_diag_principala(m)
print(f"Noua matrice : ")
for row in rezultat:
    print(row)

# Problema 6

def gaseste_x_apariti(x, *liste):
   count = {}

   for lista in liste:
      for i in lista:
         if i in count:
            count[i] += 1
         else:
            count[i] = 1

   rezultat = [i for i, apariti in count.items() if apariti == x]

   return rezultat


# Example usage:
a = [1, 2, 3]
b = [2, 3, 4]
c = [4, 5, 6]
d = [4,1, "test"]
e = ["test", 1, 7]

x = 2
rezultat = gaseste_x_apariti(x, a,b,c,d,e)
print(f"6.) {rezultat}")


# Problema 7

def este_palindrom(n):
   nr_initial = n
   oglindit = 0
   while n > 0 :
      cifra = n % 10
      oglindit = oglindit*10 + cifra
      n = n//10
   if nr_initial == oglindit :
     return True
   else :  return False

def gaseste_palindroame(lista):
   count = 0
   cel_mai_mare_palindrom = None
   for i in lista:
      if este_palindrom(i):
         count = count + 1
         if cel_mai_mare_palindrom is None or i > cel_mai_mare_palindrom:
            cel_mai_mare_palindrom = i
   return (count,cel_mai_mare_palindrom)

numere = [3663, 3456, 9119, 12332, 1111]
print(f"7.) {numere} ")
rezultat = gaseste_palindroame(numere)
print(f"Lista contine {rezultat[0]} palindroame iar {rezultat[1]} este cel mai mare.")

# Problema 8

def lista_ascii( x= 1, lista = [], flag = True):
   rezultat = []

   for i in lista:
      lista_caractere = []

      for caracter in i:
         cod_ascii=ord(caracter)
         if ( flag  == True and cod_ascii % x == 0) or ( flag  == False and cod_ascii % x != 0):
            lista_caractere.append(caracter)

      rezultat.append(lista_caractere)

   return rezultat

x = 5
lista= ["Python", "homework", "lab002", "project"]
flag = True
rezultat = lista_ascii(x,lista,flag)
print(f"8.) {lista} --> {rezultat}")

# Problema 9

def ce_spectatori_nu_pot_vedea(matrice):
   locuri = []

   for i in range(1,len(matrice)):
      for j in range(len(matrice[0])):
         spectator = matrice[i][j]
         scund = False
         for k in range(i):
            if matrice[k][j] >= spectator and scund == False:
               locuri.append((i,j))
               scund = True
   return locuri

stadion = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]
spec_scunzi = ce_spectatori_nu_pot_vedea(stadion)
print(f"9.) Locurile spectatorilor care nu pot vedea : {spec_scunzi}")

# Problema 10

def lista_de_tuple(*liste):
   rezultat = []

   for i in range(max(len(lista) for lista in liste)):
      rezultat.append(tuple(lista[i] if i < len(lista) else None for lista in liste))
   return rezultat

a = [1,2,3]
b = [5,6,7]
c = ["a", "b", "c", "d" ]

rezultat = lista_de_tuple(a,b,c)
print(f"10.) {rezultat}")

# Problema 11

def al_treilea_caracter(item):
   if len(item) >= 2 and len(item[1]) >= 3:
      return item[1][2]
   return None

def sortare(tuple):
   tuple_sortate = sorted(tuple, key=al_treilea_caracter)
   return tuple_sortate

tuple = [('abc', 'bcd'), ('abc', 'zza')]
lista_sortata = sortare(tuple)
print(f"11.) {tuple} ---> {lista_sortata}")

# Problema 12

def grupeaza_dupa_rima(cuvinte):
   grupuri = {}
   for cuvant in cuvinte:
      rima = cuvant[-2:]
      if rima in grupuri:
         grupuri[rima].append(cuvant)
      else:
         grupuri[rima] = [cuvant]
   rezultat = list(grupuri.values())
   return rezultat

cuvinte = ['ana', 'banana', 'carte', 'arme', 'parte']
rezultat = grupeaza_dupa_rima(cuvinte)
print(f"12.) {cuvinte} --> {rezultat}")