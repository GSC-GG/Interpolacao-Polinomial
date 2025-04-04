from sympy import symbols
import re

def processaPontos(pontos):

    try:
        listaPontos = re.split(';', pontos)
        listaX = []
        listaY = []

        for ponto in listaPontos :

            ponto = ponto.strip('()')
            xv = float(ponto.partition(',')[0])
            yv = float(ponto.partition(',')[2])
            listaX.append(xv)
            listaY.append(yv)

        return [listaX, listaY]
    
    except ValueError:
        print("\nValores invalidos inseridos - valores padrao foram retornados")
        return [[0],[0]]
    
def lagrange(listaX, listaY):
    x, p = symbols('x p')
    le = []
    p = 1
    f = 0

    for xi in listaX:
        for n in listaX:

            if xi != n:
                p = p * (x - n)/(xi - n)

        print("L",listaX.index(xi), '=', p)        
        le.append(p)
        p = 1

    for y in listaY:
        f = f + y * le[listaY.index(y)]

    return f