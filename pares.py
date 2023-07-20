par = 0
valores= int(input('Insira os valores :'))
for i in range(1, valores):
    if i % 2==0:
        par = par + 1
        print(i)
print('São {} números pares entre 1 até {}'.format(par,valores))
    
