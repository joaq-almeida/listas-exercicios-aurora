input_usr = input('Insira os elementos separados por espaço: ')
lista_lados = input_usr.split()

# Convertendo todos os valores em inteiro
for i in range(len(lista_lados)):
    # convertendo cada valor em inteiro
    lista_lados[i] = int(lista_lados[i])

if len(lista_lados) <= 2:
    print('Não é poligono') 
elif min(lista_lados) == max(lista_lados):
    print('Poligono regular')
else:
    print('Poligono irregular')
