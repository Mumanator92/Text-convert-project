import string

alpha = {}
def convertidor(palabra):
    """This function transforms text strings into binary code.

    Args:
        palabra (str): binary code

    >>> convertidor('Anna')
    0b1, 0b1110, 0b1110, 0b1, 
    """
    palabra = palabra.lower()
    for i, letra1 in enumerate(string.ascii_lowercase):
        alpha[letra1] = i+1
    for letra in palabra:
        print(bin(alpha.get(letra)), end=', ')

if __name__ == "__main__":
    import doctest
    doctest.testmod()