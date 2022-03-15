idade = int(input('Digite a sua idade: \n'))
bat = int(input('Digite o seu batimento: \n'))
if bat > 100 and idade > 7 or bat > 80 and idade > 17 or bat > 60 and idade > 65:
    print('Batimento está alto')
elif bat < 50 or bat < 70 and idade < 65 or bat < 80 and idade < 80 or bat < 120 and idade < 2:
    print('Batimento está baixo')
else:
    print('Seu batimento está normal')
