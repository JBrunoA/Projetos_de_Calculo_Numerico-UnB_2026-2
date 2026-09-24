# PPC-2 Método de Bairstow para encontrar raízes de polinômios
## Resumo
Código que cria uma função capaz de calcular as raízes de qualquer polinômio dado, utiliza do método de Bairstow e é capaz de criar um fractal de Bairstow das iterações necessárias para convergência no plano $(r,s)$.

## Método de Bairstow
Dado um polinômio de ordem n $f_n(x)$, como o apresentado a seguir, temos que $a_0,a_1,a_2...,a_n$ são coeficientes reais.

$$f_n(x) = a_0+a_1x+a_2x^2+...+a_nx^n$$

Podemos dividir esse mesmo polinômio por um fator quadrático $x^2-rx-s$, tal que como resultado teremos:

$$ a_0+a_1x+a_2x^2+...+a_nx^n = \left( b_2+b_3+b_4x^2+...+b_nx^{n-2} \right)(x^2-rx-s)+[b_0+b_1(x-r)]$$

De forma que o resto é dado como $R(x) = b_0+b_1(x-r)$. Podemos utilizar a seguinte relação de recorrência para a estimativa dos coeficientes $b_i$:

$$b_n = a_n$$
$$b_{n-1} = a_{n-1} + rb_n$$
$$b_i = a_i+rb_{i+1}+sb_{i+2},\ \text{para:}\ i = (n-2) \rightarrow 0$$

Sendo o objetivo encontrar valores de r e s em que $b_0$ e $b_1$ sejam nulos, podemos utilizar da série de Taylor:

$$b_1(r+\Delta r,s + \Delta s) = b_1+\frac{\delta b_1}{\delta r}\Delta r\frac{\delta b_1}{\delta s}\Delta s$$

$$b_0(r+\Delta r,s + \Delta s) = b_0+\frac{\delta b_0}{\delta r}\Delta r\frac{\delta b_0}{\delta s}\Delta s$$

Onde então buscamos valores de $\Delta r$ e $\Delta s$ que anulem $b_1(r+\Delta r,s + \Delta s)$ e $b_0(r+\Delta r,s + \Delta s)$, de tal forma então que temos as seguintes equações que formam um sistema linear:

$$-b_1 = \frac{\delta b_1}{\delta r}\Delta r\frac{\delta b_1}{\delta s}\Delta s$$
$$-b_0 = \frac{\delta b_0}{\delta r}\Delta r\frac{\delta b_0}{\delta s}\Delta s$$

Onde, podemos tratar que as derivadas são incógnitas, possibilitando a resolução pela regra de Cramer, para determinar os valores de $\Delta r$ e $\Delta s$.

$$c_1 = \frac{\delta b_0}{\delta r},\ c_1 = \frac{\delta b_1}{\delta r}={\delta b_0}{\delta s},\ c_1 = \frac{\delta b_1}{\delta s}$$

Por fim:


$$c_n = a_n$$
$$c_{n-1} = b_{n-1} + rc_n$$
$$c_i = b_i+rc_{i+1}+sc_{i+2},\ \text{para:}\ i = (n-2) \rightarrow 1$$.

Dessa forma, conseguiremos valores de $\Delta r$ e $\Delta s$ que se aproximam mais da resposta para encontrar as raízes, entretanto é necessário aplicar os passos até convergência, sendo o próximo cálculo realizado com a próxima relação de $r_i$ e $s_i$:

$$r_i = r_{i-1}+\Delta r\ \text{e}\ s_i=s_{i-1}+\Delta s$$.

Enfim, quando os valores convergem é possível calcular as raízes pela fórmula quadrática de Bhaskara, ou caso a ordem do polinômio $f_{n-1}(x)$ seja 1, pela divisão dos parâmetros (r, s).

$$x_r = \frac{r\pm \sqrt{r^2 + 4s}}{2},\ \text{para} n \ge 2$$
$$x_r = -\frac{s}{r},\ \text{para} n = 1$$.

O processo se repete até todas as raízes terem sido encontradas.


## Dicionário de Variáveis utilizadas:
### Principal
- a - Lista de coeficientes do polinômio
- r0 - Chute inicial de r
- s0 - Chute inicial de s
- b - Lista de coeficientes do polinômio transformado
- c - Lista de coeficientes da série de Taylor
- r - Valor de r atualmente sendo calculado
- s - Valor de s atualmente sendo calculado
- n - Grau do polinômio sendo calculado
- grau - Grau do polinômio original
- tol1 - Tolerância mínima para convergência de dr
- tol2 - Tolerância mínima para convergência de ds
- D - Determinante do sistema criado para cálculo pelo método de Cramer
- Dr - Determinante do sistema para cálculo de dr
- Ds - determinante do sistema para cálculo de ds
- dr - Variação de r da série de Taylor
- ds - Variação de s da série de Taylor
- ite - Número de iterações ocorridas
- xr - Lista com as raízes encontradas pelo método
### Plotagem
- var - Taxa de variação do domínio
- tot - Lista com total de iterações calculadas
- N - Valor da extremidade do domínio de cálculo
- g - Vetor de análise

## Dependências e Bibliotecas:

Foi utilizado o Numpy para cálculo e Matplotlib para geração de gráficos.

## Dados de entrada
Devem ser inseridos os seguintes dados:
#### a (lista de coeficiêntes do polinômio)
Deve ser inserido uma lista de coeficiêntes organizada do coeficiênte de maior ordem para o de menor:

$$f(x) = a_nx^n+a_{n-1}x^{n-1}+...+a_2x^2+a_1x+a_0$$
$$a=[a_n,a_{n-1},...,a_2,a_1,a_0]$$

#### r0 e s0
Devem ser escolhidos como chute inicial, o valor pode resultar no método não conseguir convergir em um valor, portanto tome cuidado quando escolher

#### plotar
Deve-se escolher se quer ou não que a função escreva no terminal quais raizes foram encontradas, True irá escrever e False não escreverá.

## Dados de saída
- Lista xr com valores das raízes encontradas
- Figura do Fractal de Bairstow das iterações calculadas

## Procedimento de Execução:

Importe a função do código caso deseje utilizá-la, também é possível rodar o código para conseguir a imagem do fractal de Bairstow

## Validação Metodológica:

O resultado é preciso para análise, os valores condizem bem com o método analítico.

## Bibliografia:

Instruções do Professor.



