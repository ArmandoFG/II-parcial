class matriz(object):
    def __init__(self):
        pass
    def matriz_n (self, n):
        if isinstance (n, int):
            return self.crear_matriz(n,1,0,[])
        else:
            return 'Error'


    def crear_matriz(self, n, contador, asterisco, resultado):
        if len(resultado)== n:
            return resultado
        elif len(resultado) < n:
            return self.crear_matriz(self, n, contador+1, asterisco+1, resultado + self.crear_aux(n, contador, asterisco, []))

    def crear_aux(self, n, contador, asterisco, resultado):
        if len(resultado) == n:
            return [resultado]
        elif len(resultado) < n:
            return self.crear_aux(n, contador, asterisco, resultado + ["*"])
        else :
            return self.crear_aux(n, contador+1, asterisco, resultado+[contador])
    
#_______________________________________________________________________________________________________________________________

class permutaciones (object):
    def __init__(self):
        pass
    def permutacion(self,n,x):
        if isinstance(n, int) and (x, int):
            return self.permutacion_aux(n,x,0,0,0)
        else:
            return 'Error'

    def permutacion_aux(self, n, x, result_n, result_x, resultado):
        if resultado != 0:
            return resultado
        elif result_n == 0:
            return self.permutacion_aux(n,x,result_n + self.fact(n,1,0), result_x, resultado)
        elif result_x == 0:
            return self.permutacion_aux(n,x,result_n, result_x + self.fact((n-x),1,0), resultado)
        else:
            return self.permutacion_aux(n,x,result_n, result_x, resultado + (result_n/result_x))

    def fact(self,num,contador,resultado):
        print(num)
        if num < contador:
            return resultado
        else:
            return self.fact(num, contador + 1, resultado*contador)
#________________________________________________________________________________________________________________________
class cuadrado (object):
    def __init__(self):
        pass
    def magico (self,matriz):
        if isinstance (matriz, list):
            return self.magico_aux(matriz,0,0,[],False, 0)
    def magico_aux(self, matriz, fila, columna, resultado, validacion, fila1):
        if validacion == True:
            return True
        elif fila <= len(matriz):
            return self.magico_aux(matriz, fila+1, columna, resultado + self.filas(matriz, fila, 0, 0), validacion, fila1)
        elif columna <= len(matriz[0]):
            return self.magico_aux(matriz, fila, columna + 1, resultado + self.columna(matriz, columna, fila1, 0), validacion, fila1)
        elif fila < 1:
            return self.magico_aux(matriz, fila, columna, resultado + self.diagonal(matriz, fila1, 0, 0), validacion, fila1 + 1)
        else:
            return self.magico_aux(matriz, fila, columna, resultado, self.validar(resultado, 0, 0), fila1)

    def filas (self, matriz, fila, columna, resultado):
        if columna == len(matriz[0]):
            return [resultado]
        else:
            return self.filas(matriz, fila, columna + 1, resultado + matriz[fila][columna])

    def columna (self, matriz, columna, fila, resultado):
        if fila == len(matriz):
            return [resultado]
        else:
            return self.columna(matriz, columna, fila + 1, resultado + matriz [fila][columna])

    def diagonal (matriz, fila, indice, resultado):
        if indice == len(matriz):
            return [resultado]
        else:
            return self.diagonal(matriz, fila, indice + 1, resultado + matriz[indice][indice])

    def validar (resultado, almacenar, indice):
        if indice == len(lista):
            return True
        elif resultado[indice] > almacenar:
            return self.validar(resultado, resultado[indice], indice + 1)
        else:
            return self.validar(resultado, almacenar, indice + 1)

#_____________________________________________________________________________________________________


class Grafico(object):
    def __init__(self):
        pass
    def grafico_aux(self, lista):
        if isinstance (lista, list):
            return self.crear_grafico(lista, 0, [], 0)
        else:
            return "Error"
    def crear_grafico(self, lista, fila, resultado, mayor):
        if len(resultado) == len(lista):
            return resultado
        elif mayor == 0:
            return  self.crear_grafico(lista, fila, resultado, mayor + self.mayor(lista, 0, 0))
        else:
            return self.crear_grafico(lista, fila, resultado + self.crear_aux(lista,lista[fila],[]), mayor)

    def mayor (self, lista, indice1, resultado):
        if indice1 == len(lista):
            return resultado
        elif lista[indice1] > resultado:
            return self.mayor(lista, indice1+1, lista[indice1])
        else:
            return self.mayor(lista, indice1+1, resultado)
    def crear_aux(self, lista, asteriscos, resultado, mayor):
        if len(resultado) == mayor:
            return [resultado]
        elif len(resultado) <= asteriscos:
            return self.crear_aux(lista, asteriscos, resultado + ["*"], mayor)
        else:
            return self.crear_aux(lista, asteriscos, resultado + [" "], mayor)
