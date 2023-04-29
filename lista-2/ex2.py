num_anterior = int(input("Digite um número inteiro: "))  # Lê um número inteiro do usuário e armazena na variável "num_anterior"
contador_de_registros = 1 # Aqui inicio a contagem dos registos dos valores
soma = num_anterior  # Inicializa a variável "soma" com o valor de "num_anterior"
num_atual = int(input("Digite outro número inteiro: "))  # Lê outro número inteiro do usuário e armazena na variável "num_atual"
contador_de_registros += 1 # Adiciona mais 1 após o input do segundo registro
soma += num_atual  # Adiciona o número lido à variável "soma"

# Inicia um loop que será executado até que o número lido seja o dobro ou a metade do número anterior
while (num_atual != (num_anterior * 2)) and (num_atual != (num_anterior / 2)):
    num_anterior = num_atual  # Atualiza o valor da variável "num_anterior" com o valor de "num_atual"
    num_atual = int(input("Digite outro número inteiro: "))  # Lê outro número inteiro do usuário e armazena na variável "num_atual"
    contador_de_registros += 1 # Adiciona mais 1 a cada nova iteração
    soma += num_atual  # Adiciona o número lido à variável "soma"

print("Quantidade de números lidos:", contador_de_registros)  # Exibe a quantidade de números lidos (que é sempre 2)
print("Soma dos números lidos:", soma)  # Exibe a soma dos números lidos
print("Valores que forçaram a parada da execução:", num_anterior, num_atual)  # Exibe os dois valores que forçaram a parada do loop
