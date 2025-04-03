"""
Núria Rodríguez Pardo
Modulo que define funciones con números primos.

>>> esPrimo(4)
False

>>> primos(20)
(2, 3, 5, 7, 11, 13, 17, 19)

>>> descompon(100)
(2, 2, 5, 5)

>>> mcm(6, 9)
18

>>> mcd(18, 16)
2

>>> mcmN(20, 2, 4)
20

>>> mcdN(50, 55, 45)
5

Las funciones deverán cumplir: 

>>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

>>> primos(50)
(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

>>> descompon(36 * 175 * 143)
(2, 2, 3, 3, 5, 5, 7, 11, 13)

>>> mcm(90, 14)
630

>>> mcd(924, 780)
12

>>> mcmN(42, 60, 70, 63)
1260

>>> mcdN(840, 630, 1050, 1470)
210
"""



def esPrimo(numero):
    """
    esPrimo retornarà True si el numero introducido es primo o False en 
    caso contrario.

    >>> esPrimo(1023)
    False

    >>> esPrimo(1021)
    True
    """

    for esDivisible in range(2, numero): # tanto el range, lonchas y demàs siempre cuentan del primero al postúltimo.
        if numero % esDivisible == 0:
            return False
    return True



def primos(numero):
    """
    primos devolverà una tupla con todos los números primos por debajo del número proporcionado, es decir, su argumento.

    >>> primos(10)
    (2, 3, 5, 7)

    >>> primos(20)
    (2, 3, 5, 7, 11, 13, 17, 19)

    """
    tupla = ()
    for buscaNum in range(2,numero):
        if esPrimo(buscaNum) == True:
            tupla += (buscaNum,)
    
    return tupla


def descompon(numero):
    """
    Devolverá una tupla con la descomposición en factores primos de su argumento.

    >>> descompon(50)
    (2, 5, 5)

    >>> descompon(500)
    (2, 2, 5, 5, 5)
    """

    factores = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        else:
            divisor += 1
            if not esPrimo(divisor):
                divisor += 1
    return tuple(factores)


def mcm(numero1, numero2):
    """
    Devolverá el mínimo común múltiplo de dos números.

    >>> mcm(4, 6)
    12
    """
    
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = set(factores1) | set(factores2)
    mcm = 1
    for factor in factores_comunes:
        potencia1 = factores1.count(factor)
        potencia2 = factores2.count(factor)
        mcm *= factor ** max(potencia1, potencia2)
    return mcm

def mcd(numero1, numero2):
    """
    Devolverá el máximo común divisor de dos números.

    >>> mcd(20, 10)
    10
    """

    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = set(factores1) & set(factores2)
    mcd = 1
    for factor in factores_comunes:
        potencia1 = factores1.count(factor)
        potencia2 = factores2.count(factor)
        mcd *= factor ** min(potencia1, potencia2)
    return mcd


def mcmN(*args):
    """
    Devolverá el mínimo común múltiplo de un número arbitrario de argumentos.

    >>> mcmN(2, 3, 10)
    30
    """

    resultado = args[0]
    for arg in args[1:]:
        resultado = mcm(resultado, arg)
    return resultado

def mcdN(*args):
    """
    Devolverá el máximo común divisor de un número arbitrario de argumentos.

    >>> mcdN(20, 30, 40)
    10
    """
    
    resultado = args[0]
    for arg in args[1:]:
        resultado = mcd(resultado, arg)
    return resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()