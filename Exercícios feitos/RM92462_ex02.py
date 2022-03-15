print('Qual é o seu tipo de assinatura? Digite:')
print('1 para Basic')
print('2 para Silver')
print('3 para Gold')
TA = int(input('4 para Platinum \n'))
# Apenas para evitar a mensagem de alerta
plano = bonus = ""
if TA != 1 and TA != 2 and TA != 3 and TA != 4:
    print('Você digitou um plano que não existe, o bonus não poderá ser calculado')
else:
    FA = float(input('Qual é o seu faturamento anual? \n'))
    if TA == 1:
        plano = 'Basic'
        bonus = FA * 0.3
    elif TA == 2:
        plano = 'Silver'
        bonus = FA * 0.2
    elif TA == 3:
        plano = 'Gold'
        bonus = FA * 0.1
    elif TA == 4:
        plano = 'Platinum'
        bonus = FA * 0.05
    print('O seu plano é o {} e o bonus a ser pago é de {:.2f}'.format(plano, bonus))
