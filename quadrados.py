import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # U

# Define o título do gráfico e nomeia os eixos
plt.title('Números Quadrados', fontsize=24)  #V
plt.xlabel('Valor', fontsize=14)  #W
plt.ylabel('Números Quadrados', fontsize=14)

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis='both', labelsize=14)  #X

plt.show()

