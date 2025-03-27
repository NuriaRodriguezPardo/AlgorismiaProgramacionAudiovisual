class Vector: 
    def __init__(self, iterable): # inicializamos el constructor con un iterable
        self._vector = [elemento for elemento in iterable]
        # con un _objeto es privado 
        # con un __objeto es aún más privado
        # return None # puedes no poner nada, porque no retorna nada igualmente o poner return a secas 

    def __repr__(self): 
        return f"vector({self._vector})"
    
    def __str__(self): # representación bonita
        cadena = "["
        for elemento in self._vector:
            cadena += f" {elemento}"
        cadena += f" ]"
        return cadena
    
    def __getitem__(self, index):
        return self._vector[index]
    
    def __setitem__(self, index, valor):
        self._vector[index] = valor

    def __len__(self):
        return len(self._vector)
    
    def __add__(self, otro):
        if isinstance(otro, (int, float, complex)):
            return Vector([elemento + otro for elemento in self._vector])
        else :
            return Vector([num1+num2 for num1, num2 in zip(self, otro)]) # zip es un objeto que nos permite recorrer dos iterables al mismo tiempo
        
    __radd__ = __add__ # para que pueda sumar de manera commutativa los iterables con el vector