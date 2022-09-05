# Napisz funkcję `cena_towaru`, która dla zadanej nazwy towaru zwróci jego cenę, jeśli taki znajduje się na liście, 
#    albo `None` jeśli towaru o podanej nazwie na liście nie ma.

# Używając funkcji `cena_towaru` napisz kod, który wczyta z klawiatury od użytkownika nazwę towaru i po naciśnięciu 
#   entera wypisze jego cenę na ekranie. Jeśli użytkownik wpisze nazwę towaru, którego nie ma na liście, program ma wypisać komunikat: "Brak towaru o podanej nazwie.".


asortyment = [
    {'nazwa': 'jabłko', 'cena': 2.49},
    {'nazwa': 'kiwi', 'cena': 23.90},
    {'nazwa': 'figa', 'cena': 3.49},
    {'nazwa': 'pomidor', 'cena': 7.49},
    {'nazwa': 'arbuz', 'cena': 3.99},
    {'nazwa': 'cytryna', 'cena': 6.99},
    {'nazwa': 'awokado', 'cena': 4.99}
]

szukaj = input("Podaj nazwę towaru:\n")

def cena_towaru (asortyment_lista, szukany_towar): 
    key = "nazwa"
 
    ## iterating through the dictionaries list with next() function: next(>>do this if A == B<<, >>else do that<<)
    target_dict = next((target_dict['cena'] for target_dict in asortyment_lista if target_dict.get(key) == szukany_towar), None)

    print(target_dict)       
    
    if target_dict == None:
        print("Brak towaru o podanej nazwie.")  

cena_towaru(asortyment, szukaj)


### WAY 2:

# def cena_towaru (asortyment_lista, szukany_towar):
#   found = 0

#   # https://careerkarma.com/blog/python-typeerror-list-indices-must-be-integers-or-slices-not-str/ :
#   for index in range(len(asortyment_lista)):
#     if asortyment_lista[index]['nazwa'] == szukany_towar:
#       print(asortyment_lista[index]['cena'])
#       found += 1
  
#   if found == 0:
#   print("Brak towaru o podanej nazwie.")   

# cena_towaru(asortyment, szukaj)

