#pip install sympy

from sympy import symbols, simplify, lambdify, init_printing
from sympy.plotting import plot
import matplotlib.pyplot as plt
from numpy import linspace
from re import split
import metodos

print("\n\tInterpolacao Polinomial\n")
print("Receba uma equacao polinomial de grau <= n que corresponda a n pontos dados\n")
print("Insira pontos na forma (x1,y1);(x2,y2);(xn,yn)")
print("Separe o x do y por virgula")
print("Separe a parte inteira da decimal de um numero por ponto\n")

pontos = input("Insira: ")
lista = metodos.processaPontos(pontos)
listaX = lista[0]
listaY = lista[1]

while 1:
    print("\nLista X:", listaX, "\nLista Y:", listaY)
    res = input("\nContinuar? (s para continuar/qualquer outro texto para cancelar) ")

    if res == 's':
        break
    pontos = input("Insira novamente: ")
    metodos.processaPontos(pontos)

while 1:
    print("Escolha o metodo de interpolacao\n")
    print("(a) Lagrange")
    print("(b) Newton")
    #print("(c) Newton-Gregory (ATENCAO - Este metodo so dara resultados corretos para pontos igualmente espacados)")

    i = input()
    match i:
        case 'a':
            print("Foi escolhido o metodo de Lagrange")
            f = metodos.lagrange(listaX, listaY)
            break #pro while, nao pro match
        case 'b':
            print("Foi escolhido o metodo de Newton")
            f = metodos.newton(listaX, listaY)
            break
        #case 'c':
        #    print("Foi escolhido o metodo de Newton-Gregory")
        #    #f = metodos.gregory(listaX, listaY)
        #    break
        case _:
            print("Opcao invalida")

print("\nFuncao: f(x) =", f, '\n')
f = simplify(f)
print("\t -- f(x) =", f, '\n')

init_printing(use_latex='png', scale=1.25, order='grlex')

for n in listaX:
    n = float(n)

for n in listaY:
    n = float(n)


x = symbols('x')

listaX_ordenada = sorted(listaX)
x_inicio = int(listaX_ordenada[0]) - 100
x_fim = int(listaX_ordenada[-1]) + 100
pontos = (x_fim - x_inicio) * 10  # 10 ou 100 pontos por unidade, como preferir

f_lambdify = lambdify(x, f, "numpy")

x_vals = linspace(x_inicio, x_fim, pontos)
y_vals = f_lambdify(x_vals)
plt.plot(x_vals, y_vals)
plt.scatter(listaX, listaY)
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.grid(True)
plt.show()

print("O grafico da funcao nao abrange os pontos corretamente? Analise se os pontos inseridos constituem de fato uma funcao\n")

#(0,4);(0.2,3.84);(0.4,3.76)