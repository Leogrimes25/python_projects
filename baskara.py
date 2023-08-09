import math
A, B, C = map(float, input().split())
delta = B ** 2 - (4 * A * C)
if A and B and C and delta > 0.0:
    r1 = (-B + math.sqrt(delta)) / (2 * A)
    r2 = (-B - math.sqrt(delta)) / (2 * A)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))
else:
    print('Impossivel calcular')