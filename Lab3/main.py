# Problema 1
# Write a function that receives as parameters two lists a and b and returns a list of sets containing:
# (a intersected with b, a reunited with b, a - b, b - a)

a = [1, 3, 4, 5, 8, 9, 10]
b = [2, 4, 5, 6, 7, 8]

print(f"1.) Lista a: {a}")
print(f"Lista b: {b}")


def operatii_liste(a, b):
    a = set(a)
    b = set(b)

    intersectia = a.intersection(b)
    reuniunea = a.union(b)
    a_minus_b = a.difference(b)
    b_minus_a = b.difference(a)

    return intersectia, reuniunea, a_minus_b, b_minus_a


rezultat = operatii_liste(a, b)
print(f"Intersectia lui a si b: {rezultat[0]}")
print(f"Reuniunea lui a si b: {rezultat[1]}")
print(f"a - b : {rezultat[2]}")
print(f"b - a : {rezultat[3]}")


# Problema 2

def nr_caractere(text):
    count = {}
    for caracter in text:
        if caracter in count:
            count[caracter] += 1
        else:
            count[caracter] = 1
    return count


text = "Tema la Python."
print(f"2.) Textul: {text}")
rezultat = nr_caractere(text)
print(rezultat)


# Problema 3

def compare_dictionaries(dict1, dict2):
    if type(dict1) != type(dict2):
        return False
    if isinstance(dict1, dict):
        if set(dict1.keys()) != set(dict2.keys()) or len(dict1) != len(dict2):
            return False

        for i in dict1.keys():
            if not compare_dictionaries(dict1[i], dict2[i]):
                return False
    elif isinstance(dict1, (list, set)):
        if len(dict1) != len(dict2):
            return False
        for i, j in zip(dict1, dict2):
            if not compare_dictionaries(i, j):
                return False
    else:
        if dict1 != dict2:
            return False
    return True

dict1 = {'x': 1, 'y': 2, 'z': { 'k' : 3}}
dict2 = {'x': 1, 'z': { 'k' : 3}, 'y': 2}

dict3 = {'x': [2, 4], 'y': 6, 'z': 8}
dict4 = {'y': 6,'x': [2, 4], 'z': 10}
rezultat1 = compare_dictionaries(dict1,dict2)
rezultat2 = compare_dictionaries(dict3,dict4)
print(f"3.) {rezultat1}")
print(f"{rezultat2}")

# Problema 4

def build_xml_element(tag, content, elements):
    xml_element = f"<{tag} "

    for i, valoare in elements.items():
        xml_element += f'{i}="{valoare}\\"'

    xml_element += f">{content}"

    return xml_element

rezultat = build_xml_element("a", "Hello there", {'href': "http://python.org", '_class' : "my-link", 'id' : "someid"})
print(f"4.) {rezultat}")

# Problema 5

# Problema 6

def nr_unice_duplicate(lista):
    unice = set()
    duplicate = set()

    for i in lista:
        if i in unice:
            duplicate.add(i)
        else:
            unice.add(i)

    return len(unice), len(duplicate)

a = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"6.) {a}")
rezultat = nr_unice_duplicate(a)
print(f"{rezultat}")


# Problema 7

def set_operatii(*sets):
    rezultat = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]

            rezultat[f"{set1} | {set2}"] = set1 | set2
            rezultat[f"{set1} & {set2}"] = set1 & set2
            rezultat[f"{set1} - {set2}"] = set1 - set2
            rezultat[f"{set2} - {set1}"] = set2 - set1

    return rezultat

set1 = {1, 2}
set2 = {2, 3}
print(f"7.) {set1} , {set2}")
rezultat = set_operatii(set1, set2)
for i, valoare in rezultat.items():
    print(f"{i}: {valoare}")

# Problema 8
def loop(mapping):
    vizitat = set()
    rezultat = []

    cheie_curenta = "start"

    while cheie_curenta in mapping and cheie_curenta not in vizitat:
        vizitat.add(cheie_curenta)
        rezultat.append(cheie_curenta)
        cheie_curenta = mapping[cheie_curenta]

    return rezultat

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
print(f"8.) {mapping}")
rezultat = loop(mapping)
print(f" {rezultat}")

# Problema 9

def count_matches(*positional_args, **keyword_args):
    valori = set(keyword_args.values())
    count = 0

    for argument in positional_args:
        if argument in valori:
            count += 1

    return count


args = (1, 2, 3, 4)
kwargs = {"x": 1, "y": 2, "z": 3, "w": 5}
print(f"9.) Exemplu : {args} , {kwargs}")
rezultat = count_matches(*args,**kwargs)
print(f"Rezultat: {rezultat}")