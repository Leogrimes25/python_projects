A, B, C = (map(float, input().split()))
pi = 3.14159
Atrianguloretangulo = A * C / 2
ATrapezio = (A + B) * C / 2
Acirculo = pi * C * C
Aquadrado = B * B
Aretangulo = A * B
print('TRIANGULO: {:.3f}'.format(Atrianguloretangulo))
print(('CIRCULO: {:.3f}'.format(Acirculo)))
print('TRAPEZIO: {:.3f}'.format(ATrapezio))
print('QUADRADO: {:.3f}'.format(Aquadrado))
print('RETANGULO: {:.3f}'.format(Aretangulo))