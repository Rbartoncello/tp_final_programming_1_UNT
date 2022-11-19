from constantes import *

x = 660
y = 507

w = 44
h = 38
amount = 4

dict = {
    "x": x,
    "y": y,
    "width": w,
    "height": h,
    "path": "PIXEL ADVENTURE/Recursos/Terrain/Block/2.png",
    "type": 1
}

lista = []
lista_final = []

for i in range(amount):
    dict_2 = dict.copy()

    dict_2['x'] += i * w

    lista.append(dict_2)

final = '{'
for dict_final in lista:

    for key in dict_final:
        if type(dict_final[key]) == type(str()):
            final += '"{}": "{}", '.format(key, dict_final[key])
        else:
            final += '"{}": {}, '.format(key, dict_final[key])
    final = final[:len(final) - 2]
    final += '},\n{'
    lista_final.append(final)
final = final[:len(final) - 3]

archivo = open('generado_plataformas.json', 'w')
archivo.write(final)
