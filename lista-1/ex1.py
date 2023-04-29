import math

metros_quadrados = int(input("Entre com a área em metros quadrados: "))
tipo_azulejo = int(input("Entre com o tipo de azulejo: "))

qtd_caixas = 0

if metros_quadrados <= 0:
    print("Valor de metros quadrados é inválido!!!")
    
if tipo_azulejo > 3 or tipo_azulejo < 1:
    print("Tipo de azulejo é inválido!!!")

if tipo_azulejo == 1:
    qtd_caixas = (metros_quadrados/2 * 10)

if tipo_azulejo == 2:
    qtd_caixas = (metros_quadrados/3 * 10)

if tipo_azulejo == 3:
    qtd_caixas = (metros_quadrados/4 * 10)

print("QTD de azulejos necessários: ", math.ceil(qtd_caixas))
