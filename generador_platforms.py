from constantes import *

dict = {
    "x": 20,
    "y": 10,
    "width": 10,
    "height": 20,
    "path": "PIXEL ADVENTURE/Recursos/Terrain/Wall/2.png",
    "type": 1
}

lista = []
lista_final = []

for i in range(int(22)):
    dict_2 = dict.copy()

    dict_2['y'] += i * 20

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
