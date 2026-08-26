# PPC 1 - Método de RUnge-Kutta para uma partícula sedimentando
## Resumo:

Código que utiliza do método de Runge-Kutta para calcular a velocidade de uma partícula ao longo do tempo até sua velocidade terminal. Foi calculado baseado na equação adimensionalizada para escoamenteo em $RE\approx1$, essa é dada por:

$$ St\frac{dv_z^\*}{dt^\*} = 1+ -v_z^\* - \frac{3}{8}Rev_z^{2\*} $$

onde suas variáveis são:

- $Re$: Número de Reynolds
- $St$: Número de Stokes
- $v_z^\*$: Velocidade adimensional
- $t^\*$: Tempo adimensional

Sendo a solução analítica para o caso apresentado em duas possíveis formas, para $Re << 1$:

$$ v_z^\* = 1 - e^{-t/St} $$

assim como para o caso de $Re \approx 1$, em que será utilizada apenas o valor da velocidade terminal adimensional para a análise:

$$ v_z^\* = \frac{-1+\sqrt{1+(\frac{3}{2}Re)}}{\frac{3}{4}Re} $$

## Método de Runge-Kutta

O método para solução numérica utilizado consiste em calcular equações diferenciais ordinárias do tipo:

$$ \frac{dy}{dt} = f(t,v) $$

Utilizando como equações:

$$ v_{i+1} = v_i+\frac{1}{6}(k_1+2k_2+2k_3+k_4)\Delta t $$

e

$$ k_1 = f(t_i, v_i), \quad k_2 = f\left(t_i+\Delta t/2,v_i+k_1\Delta t/2\right), $$
$$ k_3 = f\left(t_i+\Delta t/2,v_i+k_2\Delta t/2\right), k_4 = f\left(t_i+\Delta t,v_i+k_3\Delta t\right). $$

## Dicionário de Variáveis utilizadas:

- Re - Número de Reynolds
- St - Número de Stokes
- vo - Velocidade inicial
- Dt - Passo do tempo
- k1, k2, k3, k4 - Coeficientes para cálculo de método de Runge Kutta
- vp - Velocidade posterior, a velocidade calculada no instante da iteração
- va - Velocidade anterior, a velocidade calculada na iteração anterior
- velocidades - Lista de valores da velocidade
- tempo - Lista de valores do tempo
- i - contador de iterações
- terminal - Variável para controlar o loop
- velocidade_teorica - Lista de valores da velocidade calculada por método analítico
- t - Tempo que está sendo calculado na iteração
- v_teo - Velocidade teóriaca em um ponto do tempo
- num_var_t - Número de variações no passo de tempo
- tax_var_Dt - Taxa de variação do passo de tempo
- Dt_var - Lista com as variações de Dt
- num_var_Re - Número de variações no passo de Re
- Re_var - Lista com as variações de Re
- tax_var_Re - Taxa de variação do passo de Re
- velocidades_var - Lista contendo todas as listas de velocidades variadas por Re ou Dt
- tempos_var - Lista contendo todas as listas de tempos variadas por Re ou Dt

## Dependências e Bibliotecas:

Foi utilizado o Numpy para cálculo e Matplotlib para geração de gráficos.

## Entradas e Saídas:

As variaveis de entrada são entrada são:
- Re
- St
- vo
- Dt
- Número de variações de Re
- Número de variações de Dt
- Taxa de variação de Dt
- Taxa de variação de Re

As de saída são:
- velocidades
- velocidade_teorica
- tempo

### Dados de Entrada:

Os dados esperados para entrada são apenas as variáveis físicas, sendo necessário alterar seus valores no início do códgo.

### Dados de Saída:

São criadas as listas de velocidade e tempo para o caso numérico e analítico, assim como gráficos comparando a velocidade com o tempo. Dos gráficos criados, temos:

- Velocidade numérica
- Comparação de velocidade numérica e teórica
- Comparação entre variados valores de Dt
- COmparação entre variados valores de Re

## Procedimento de Execução:

Rode o código em um ambiente Python

## Validação Metodológica:

O resultado é preciso para análise, os valores condizem bem com o método analítico.

## Bibliografia:

Instruções do Professor.
