import string

alpha = {}
def convertidor(palabra):
    palabra = palabra.lower()
    for i, letra1 in enumerate(string.ascii_lowercase):
        alpha[letra1] = i+1
    for letra in palabra:
        print(bin(alpha.get(letra)), end=', ')

convertidor('Anna')