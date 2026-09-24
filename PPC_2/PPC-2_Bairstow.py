import numpy as np
import matplotlib.pyplot as plt

def Bairstow(a, r0, s0, printar=True):

    #Cálculo por método de Cramer
    def cramer(c,b):
        b = b
        D = (c[0][0]*c[1][1])-(c[0][1]*c[1][0])
        Dr = (-b[0]*c[1][1])-(-b[1]*c[0][1])
        Ds = (-b[1]*c[0][0])-(-b[0]*c[1][0])
        return [Dr/D, Ds/D]    
    
    #inverter lista para calculos
    a = a[::-1]     
    #variaveis iniciais
    n = len(a)-1
    grau = n
    #Assumindo o valor inicial antes do loop
    r = r0
    s = s0
    #Tolerâncias do problema
    tol1 = 10e-4
    tol2 = 10e-4
    #Lista com valores de raizes
    xr = []

    ite = 0

    while len(xr) < grau:
        #Para o caso de a equação ser diretamente de primeiro ou segundo grau, é necessário calculà-las por suas soluções normais.
        if n == 2:
            delta = a[1]**2-4*a[2]*a[0]     #delta da equação de Bhaskara
            if delta >= 0:
                #Cálculo para raizes reais
                xr.append((-a[1]+np.sqrt(delta))/(2*a[2]))
                xr.append((-a[1]-np.sqrt(delta))/(2*a[2]))
            else:
                #Raizes imaginárias
                xr.append(complex(-a[1]/(2*a[2]), np.sqrt(-delta)/(2*a[2])))
                xr.append(complex(-a[1]/(2*a[2]), -np.sqrt(-delta)/(2*a[2])))
            break
        if n == 1:
            xr.append(-a[0]/a[1])
            break

        #Para qualquer polinômio de ordem maior que 2 teremos então:
        #calculo de b
        b = [0] * (n+1)
        b[n] = a[n]
        b[n-1] = a[n-1]+r*b[n]
        for i in range(n-2, -1, -1):
            b[i] = a[i] + r*b[i+1]+s*b[i+2]

        #calculo de c
        c = [0] * (n+1)
        c[n] = b[n]
        c[n-1] = b[n-1]+r*c[n]
        for i in range(n-2, -1, -1):
            c[i] = b[i] + r*c[i+1]+s*c[i+2]

        #Temos que calcular um sistema linear pelo método de Cramer
        C = [[c[1],c[2]],[c[2],c[3]]] #Matriz C para calulo pelo método de cramer
        dr, ds = cramer(C,b)

        #Substituição para novos r e s
        r += dr
        s += ds
        #Avaliação de convergência
        if np.abs(dr) <= tol1*(1+np.abs(r)) and np.abs(ds) <= tol2*(1+np.abs(s)):

            #Cálculo principal utilizando da fórmula de Bhaskara
            delta = r**2+4*s   #Esse é o delta dentro do Bhaskara
            if delta >= 0:
                #Cálculo para raizes reais
                xr.append((r+np.sqrt(delta))/2)
                xr.append((r-np.sqrt(delta))/2)
            else:
                #Raizes imaginárias
                xr.append(complex(r/2, np.sqrt(-delta)/2))
                xr.append(complex(r/2, -np.sqrt(-delta)/2))

            #Altera a lista de [a] e atualiza o valor de n
            a = b[2:]   #Só queremos os valores excluindo os primeiros 2
            n = len(a)-1

            #Resetar para próxima iteração
            r = r0
            s = s0

        ite += 1

        #Para o caso do valor não convergir e as iterações subirem muito
        if ite >= 25:
            break
    if printar == True:
        print("Raízes do polinômio:")
        for i in range(len(xr)):
            print(f'Raiz n° {i+1}:', f"{xr[i]:.4f}")
        print('Número de itereações:', ite)

    return xr, ite

#----------------------------------Análise vibratória------------------------------
def vibes(a, r0, s0):
    #calcula os valores de xr
    xr, ite = Bairstow(a, r0, s0)
    #Avalia qual o comportamento do sistema:
    #Caso tenha resultados imaginários
    if type(xr[0]) == complex:
        if (xr[0] + xr[1]).imag == 0:   #Raizes conjugadas dão 0
            print('Sistema Subamortecido')
        else:
            print('Sistema Harmônico')
    else:
        if xr[0] == xr[1]:
            print('Sistema Criticamente Amortecido')
        else:
            print('Sistema Super Amortecido')
    
    print('Primeira raiz:', xr[0])
    print('segunda raiz:', xr[1])

#-----------------------------Avaliação de imagem------------------------------------

#lista com os coeficientes do polinômio
#Coloque os coeficientes na ordem de maior coeficiênte de x para menor x^n --> x^0
a = [1,4,-62,-200,1009,2356,-3828,-5040]

#Número de avaliação
#será feito de 1 em 1, varia r e varia s logo em seguida, construindo uma escada
N = 5
var = .1
tot = []

#vetor de análise
g = np.arange(-N, N, var)
for i in g:
    r0 = i
    par = []
    for j in g:
        s0 = j
        xr, ite = Bairstow(a, r0, s0, False)
        par.append(ite)
    tot.append(par)

plt.figure()
plt.imshow(tot, extent=[-N, N, -N, N], origin="lower")
plt.colorbar(label='n° de Iterações')
plt.show()

#----------------------- Análise vibratória --------------------------------
r0 = 0.1
s0 = r0
vibes(a, r0, s0)