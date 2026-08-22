import matplotlib.pyplot as plt
import numpy as np

#Valores de entrada
Re = 1
St = 1
vo = 0
Dt = 0.1

#Funcoes basicas
#funcao para calcular o valor de ki(v)
def ki(v, Re, St):
    return (1/St) - (v/St) - (3/8)*(Re/St)*(v**2)

#funcao para calcular vp no instante Dt
def vp(v, Re, St, Dt):
    k1 = ki(v, Re, St)
    k2 = ki(v + (Dt/2)*k1, Re, St)
    k3 = ki(v + (Dt/2)*k2, Re, St)
    k4 = ki(v + Dt*k3, Re, St)
    return v + (Dt/6)*(k1 + 2*k2 + 2*k3 + k4)

#calculo principal numerico
velocidades = []  #lista para armazenar os valores de velocidade
tempo = []        #lista para armazenar os valores de tempo

i = 0   #contador de iteracoes
terminal = False  #variavel para controlar o loop principal
#loop principal
while terminal != True:
    if i == 0:
        velocidades.append(vo)  #adiciona a velocidade inicial na lista
        tempo.append(0)          #adiciona o tempo inicial na lista
    else:
        velocidades.append(vp(velocidades[i-1],Re,St,Dt)) #adiciona a velocidade posterior na lista
        tempo.append(tempo[i-1] + Dt)  #adiciona o tempo na lista

    if i >= 2:  #verifica se ja existem pelo menos 2 valores de velocidade para comparar
        if np.abs(velocidades[i] - velocidades[i-1])/velocidades[i-1] < 1e-4: #compara valores até que a velocidade estabilize
            terminal = True

    i += 1  #incrementa o contador de iteracoes

#calculo do valor teorico de velocidade
velocidade_teorica = []
if Re == 0:
    for t in tempo:
        velocidade_teorica.append(1 - np.exp(-t/St)) #equacao para velocidade adimensionam em Re = o
else:
    for t in tempo: 
        v_teo = (-1+np.sqrt(1+(3/2*Re)))/(3/4*Re)   #variavel intermediária para a lista
        velocidade_teorica.append(v_teo) #velocidade adimensional maxima para RE ~ 0

        #gerador de graficos
#grafico puramente numerico
plt.figure()
plt.plot(tempo, velocidades)
plt.title('Gráfico de Velocidade x Tempo numérico')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (--)')
plt.grid()
plt.show()

#grafico puramente numerico
plt.figure()
plt.plot(tempo, velocidades, 'co')
plt.plot(tempo, velocidade_teorica, 'r-')
plt.title('Gráfico de Velocidade x Tempo numérico')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (--)')
plt.grid()
plt.show()
