altura = float(input("Insira a altura do seu reservatório em cm:"))
largura = float(input("Insira a largura do seu reservatório em cm:"))
comprimento = float(input("Insira o comprimento do seu reservatório em cm:"))

capacidade = (altura * largura * comprimento)/1000

consumo_diario = float(input("Insira o consumo médio diário em litros/dia:"))

autonomia = capacidade / consumo_diario

print('A capacidade do reservatório é de', capacidade, 'litros.', 'Possui uma autonomia de', autonomia, 'dias.', 'E você possui um')

if autonomia < 2 :
  print('Consumo elevado.')
elif 2 <= autonomia < 7 :
  print('Consumo moderado.')
elif 7 <= autonomia :
  print('Consumo reduzido.')
