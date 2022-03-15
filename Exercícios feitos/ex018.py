import math
a2 = float(input('Digite um angulo em graus: '))
a = math.radians(a2)
cosa = math.cos(a)
sena = math.sin(a)
tga = math.tan(a)
print('O sen(a) é {:2f}, o cos(a) é {:2f} e a tan(a) é {:2f}'.format(sena, cosa, tga))
