import math
a = float(input('Digite a medida do cateto oposto à hipotenusa: '))
b = float(input('Digite a medida do cateto adjacente à hipotenusa: '))
print('A hipotenusa mede {}'.format((a**2+b**2)**(1/2)))
print('A hipotenusa mede {}'.format(math.sqrt(a**2+b**2)))
print('A hipotenusa mede {}'.format(math.hypot(a, b)))
