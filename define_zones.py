ocorrencias=[163,158,158,174,132,149,165,158,153,161,121]
zone_1=[]
zone_2=[]
zone_3=[]
zone_4=[]
zone_5=[]

count_zona_1 = 0
count_zona_2 = 0
count_zona_3 = 0
count_zona_4 = 0
count_zona_5 = 0

for elemento in ocorrencias:
    if elemento <=145:
        zone_1.append(elemento)
        count_zona_1 +=1

    elif elemento >=146 and elemento <=158:
        zone_2.append(elemento)
        count_zona_2 +=1

    elif elemento>=159 and elemento <=170:
        zone_3.append(elemento)
        count_zona_3 +=1

    elif elemento>=171 and elemento <=180:
        zone_4.append(elemento)
        count_zona_4 +=1

    elif elemento >180:
        zone_5.append(elemento)
        count_zona_5 +=1

def distribution():
    print("Estão dentro da Zona 1 as ocorrencias :",zone_1)
    print("O número de ocorrencias em Zona 1 é :",count_zona_1)
    calculo_zona_1= (count_zona_1/11) * 100
    print("Sendo assim o atleta pedalou {:.2f} em porcentagem".format(calculo_zona_1))
    
    print('')

    print("Estão dentro da Zona 2 as ocorrencias :",zone_2)
    print("O número de ocorrencias em Zona 1 é :",count_zona_1)
    calculo_zona_2= (count_zona_2/11) * 100
    print("Sendo assim o atleta pedalou {:.2f} em porcentagem".format(calculo_zona_2))
    
    print('')

    print("Estão dentro da Zona 3 as ocorrencias :",zone_3)
    print("O número de ocorrencias em Zona 1 é :",count_zona_3)
    calculo_zona_3= (count_zona_3/11) * 100
    print("Sendo assim o atleta pedalou {:.2f} em porcentagem".format(calculo_zona_3))

    print('')

    print("Estão dentro da Zona 4 as ocorrencias :",zone_4)
    print("O número de ocorrencias em Zona 1 é :",count_zona_4)
    calculo_zona_4= (count_zona_4/11) * 100
    print("Sendo assim o atleta pedalou {:.2f} em porcentagem".format(calculo_zona_4))
    
    print('')

    print("Estão dentro da Zona 5 as ocorrencias :",zone_5)
    print("O número de ocorrencias em Zona 1 é :",count_zona_5)
    calculo_zona_5= (count_zona_5/11) * 100
    print("Sendo assim o atleta pedalou {:.2f} em porcentagem".format(calculo_zona_5))



distribution()

    

