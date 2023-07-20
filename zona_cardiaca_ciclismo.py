value_age = int(input('Insira a sua idade :'))

formula_tanaka = 208 - (0.7 * value_age)

zone_1 = 0.0, formula_tanaka * 0.65

zone_2 = formula_tanaka * 0.66, formula_tanaka * 0.75

zone_3 = formula_tanaka * 0.76, formula_tanaka * 0.85

zone_4 = formula_tanaka * 0.86, formula_tanaka * 0.90

zone_5 = formula_tanaka * 0.9, formula_tanaka * 1.0

print('Minha Zona 1 varia entre {:.2f} e {:.2f} batimentos cardíacos'.format(zone_1[0], zone_1[1]))

print('Minha Zona 2 varia entre {:.2f} e {:.2f} batimentos cardíacos'.format(zone_2[0], zone_2[1]))

print('Minha Zona 3 varia entre {:.2f} e {:.2f} batimentos cardíacos'.format(zone_3[0], zone_3[1]))

print('Minha Zona 4 varia entre {:.2f} e {:.2f} batimentos cardíacos'.format(zone_4[0], zone_4[1]))

print('Minha Zona 5 varia entre {:.2f} e {:.2f} batimentos cardíacos'.format(zone_5[0], zone_5[1]))
