from math import sqrt
import random
n = float(input('Digite um número: '))
raiz = sqrt(n)
print('A raiz de {} é {:.2f}'.format(n, raiz))
n2 = random.randint(1, 10)
n3 = random.randint(1, 10)
print(n2**2+n3*2)
n4 = input('Quanto é n2+n3?')
print('n2 = {} e n3 = {}'.format(n2, n3))

