input_usr = input('Insira os elementos separados por espaço: ')
lista_lados = input_usr.split()

## Abaixo temos duas formas de lidar com a lista de dados inserida pelo usuario
## A primeira utiliza o laço de repetição 'FOR', já a seguinda utiliza 'WHILE'
## Ambas funcionam.

# Convertendo todos os valores em inteiro
# for i in range(len(lista_lados)):
#     # convertendo cada valor em inteiro
#     lista_lados[i] = int(lista_lados[i])

# Convertendo todos os valores em inteiro
indice = 0
while indice < len(lista_lados):
    # convertendo cada valor em inteiro
    lista_lados[indice] = int(lista_lados[indice])
    indice = indice + 1

if len(lista_lados) <= 2:
    print('Não é poligono')
    
elif min(lista_lados) == max(lista_lados):
    print('Poligono regular')
    
else:
    print('Poligono irregular')
