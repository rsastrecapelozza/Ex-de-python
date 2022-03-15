import random
nv = seg1 = ter1 = qua1 = qui1 = sex1 = 1
# Apenas para evitar o aviso de que as variaveis podem ser indefinidas (apesar de que não poderiam)
seg = ter = qua = qui = sex = 0
while nv >= 1:
    if seg1 == 1:
        seg = int(input('Digite o número de votos na Segunda-Feira:  '))
    if ter1 == 1:
        ter: int = int(input('Digite o número de votos na Terça-Feira:  '))
    if qua1 == 1:
        qua = int(input('Digite o número de votos na Quarta-Feira:  '))
    if qui1 == 1:
        qui = int(input('Digite o número de votos na Quinta-Feira:  '))
    if sex1 == 1:
        sex = int(input('Digite o número de votos na Sexta-Feira:  '))
    total = seg + ter + qua + qui + sex
    if seg > ter and seg > qua and seg > qui and seg > sex:
        print('O dia vencedor foi segunda-feira, com {} ("{:.2f}%") voto(s)! '.format(seg, (seg/total)*100))
        nv = 0
    elif ter > seg and ter > qua and ter > qui and ter > sex:
        print('O dia vencedor foi terça-feira, com {} ("{:.2f}%") voto(s)! '.format(ter, (ter/total)*100))
        nv = 0
    elif qua > seg and qua > ter and qua > qui and qua > sex:
        print('O dia vencedor foi quarta-feira, com {} ("{:.2f}%") voto(s) voto(s)!'.format(qua, (qua/total)*100))
        nv = 0
    elif qui > seg and qui > ter and qui > qua and qui > sex:
        print('O dia vencedor foi quinta-feira, com {} ("{:.2f}%") voto(s) voto(s)!'.format(qui, (qui/total)*100))
        nv = 0
    elif sex > seg and sex > ter and sex > qua and sex > qui:
        print('O dia vencedor foi sexta-feira, com {} ("{:.2f}%") voto(s) voto(s)!'.format(sex, (sex/total)*100))
        nv = 0
    else:
        seg1 = ter1 = qua1 = qui1 = sex1 = 0
        print('Houve empate na votação! Os dias mais votados foram: ')
        if seg >= ter and seg >= qua and seg >= qui and seg >= sex:
            print('Segunda-feira')
            seg1 = 1
        if ter >= seg and ter >= qua and ter >= qui and ter >= sex:
            print('Terça-feira')
            ter1 = 1
        if qua >= seg and qua >= ter and qua >= qui and qua >= sex:
            print('Quarta-feira')
            qua1 = 1
        if qui >= seg and qui >= ter and qui >= qua and seg >= sex:
            print('Quinta-feira')
            qui1 = 1
        if sex >= seg and sex >= ter and sex >= qua and sex >= qui:
            print('Sexta-feira')
            sex1 = 1
        print('Para uma nova votação entre os dias empatados digite 1')
        print('Para escolher aleatóriamente um dos dias mais votados digite 2')
        var1 = int(input('Para finalizar sem desempatar digite 3 \n'))
        if var1 == 1:
            print('Ok vamos para a nova votação!')
        elif var1 == 2:
            seg2 = ter2 = qua2 = qui2 = sex2 = 0
            opcao = 0
            if seg1 == 1:
                opcao = opcao + 1
                seg2 = opcao
            if ter1 == 1:
                opcao = opcao + 1
                ter2 = opcao
            if qua1 == 1:
                opcao = opcao + 1
                qua2 = opcao
            if qui1 == 1:
                opcao = opcao + 1
                qui2 = opcao
            if sex1 == 1:
                opcao = opcao + 1
                sex2 = opcao
            dia = random.randrange(1, (opcao+1))
            if dia == seg2:
                print('O dia escolhido aleatóriamente foi segunda-feira!')
            elif dia == ter2:
                print('O dia escolhido aleatóriamente foi terça-feira!')
            elif dia == qua2:
                print('O dia escolhido aleatóriamente foi quarta-feira!')
            elif dia == qui2:
                print('O dia escolhido aleatóriamente foi quinta-feira!')
            elif dia == sex2:
                print('O dia escolhido aleatóriamente foi sexta-feira!')
            nv = 0
        elif var1 == 3:
            nv = 0
