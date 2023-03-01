def soma_diagonal_principal(matriz):
    resultado=0
    for i in range(len(matriz)):
        if len(matriz) == len(matriz[i]):
            resultado= matriz[0][0]+matriz[1][1]+matriz[2][2]
            return resultado
        else:
            return -1

MatrizInt= [[1,2],[4,5]]

res=soma_diagonal_principal(MatrizInt) 

assert res == 6