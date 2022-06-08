#visualizando dados
#tabela basica

import matplotlib.pyplot as plt

x = [1, 2, 5, 9, 14]
y = [2, 4, 6, 8, 10]

#legenda título
plt.title("Meu primeiro gráfico com Python")
#legendas nos eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

#plt.bar ---> gráfico de barras
#plt.plot ---> gráfico de linhas
plt.plot(x, y)
plt.show()

