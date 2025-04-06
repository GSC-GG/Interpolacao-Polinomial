from sympy import symbols
from math import factorial, pow
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

i = -1

def newton(listaX, listaY):

    class ArvNewton:
        def __init__(self, valor = None, xvDir = None, xvEsq = None):
            self.valor = valor
            self.paiDir = None
            self.paiEsq = None
            self.xvDir = xvDir
            self.xvEsq = xvEsq

    def criaArv(n):
        global i
        if n == 1:
            i += 1
            return ArvNewton(valor = listaY[i], xvDir = listaX[i], xvEsq = listaX[i])
        od = ArvNewton()
        od.paiDir = criaArv(n-1)
        od.paiEsq = criaArv(n-1)
        od.xvDir = od.paiDir.xvDir
        od.xvEsq = od.paiEsq.xvEsq
        od.valor = (od.paiEsq.valor - od.paiDir.valor) / (od.xvEsq - od.xvDir)
        i -= 1
        return od
    
    odn = criaArv(len(listaX))
    od = odn
    j = len(listaX) - 1
    f = 0
    x, d = symbols('x d')
    
    while j >= 0:
        d = od.valor
        k = 0
        while k < j:
            d *= (x - listaX[k])
            k += 1
        f += d
        od = od.paiDir
        j -= 1
        
    return f

def gregory(listaX, listaY):

    h = listaX[1] - listaX[0]

    n = 1
    while n < len(listaX) - 1:
        if listaX[n+1] - listaX[n] != h:
            print("Pontos dados nao sao igualmente espacados")
        n += 1

    class ArvNewton:
        def __init__(self, valor = None):
            self.valor = valor
            self.paiDir = None
            self.paiEsq = None

    def criaArv(n):
        global i
        if n == 1:
            i += 1
            return ArvNewton(valor = listaY[i])
        od = ArvNewton()
        od.paiDir = criaArv(n-1)
        od.paiEsq = criaArv(n-1)
        od.valor = (od.paiEsq.valor - od.paiDir.valor) / (h * (n-1))
        i -= 1
        return od
    
    odn = criaArv(len(listaX))
    od = odn
    j = len(listaX) - 1
    f = 0
    x, d = symbols('x d')
    
    while j >= 0:
        d = od.valor
        k = 0
        while k < j:
            d *= (x - listaX[k])
            k += 1
        f += d
        od = od.paiDir
        j -= 1
        
    return f