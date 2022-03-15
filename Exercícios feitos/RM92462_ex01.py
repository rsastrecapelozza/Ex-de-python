peso = int(input('Digite o seu peso: \n'))
altura = float(input('Digite a sua altura: \n'))
IMC = peso / altura**2
print('O seu IMC é {:.2f}'.format(IMC))
if IMC < 16.00:
    print('Esse IMC é classificado como "Baixo peso grau III"')
elif IMC < 17.00:
    print('Esse IMC é classificado como "Baixo peso grau II"')
elif IMC < 18.50:
    print('Esse IMC é classificado como "Baixo peso grau I"')
elif IMC < 25.00:
    print('Esse IMC é classificado como "Peso ideal"')
elif IMC < 30.00:
    print('Esse IMC é classificado como "Sobrepeso"')
elif IMC < 35.00:
    print('Esse IMC é classificado como "Obesidade grau I"')
elif IMC < 40.00:
    print('Esse IMC é classificado como "Obesidade grau II"')
else:
    print('Esse IMC é classificado como "Obesidade grau III"')
