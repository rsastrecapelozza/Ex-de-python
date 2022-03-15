v1 = int(input('Qual é a velocidade do veículo?  '))
if v1 > 80:
    print('MULTADO!!! Você excedeu o limite de velocidade de 80 km/h. O Valor da multa será de {.2f} '.format((v1-80)*7))
else:
    print('Dirija com cuidado e tenha um bom dia!')
