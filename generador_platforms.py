from constantes import *

dict = {	
	"x": 0,
	"y": 0,
	"width": 40,
	"height": 40,
	"path": "PIXEL ADVENTURE/Recursos/Terrain/2.png",
	"type": 1
}

lista = []

for i in range(int(H_WINDOWN/40)):
    dict_2 = dict.copy()
    
    dict_2['y'] += i * 40
    
    lista.append(dict_2)
    
for i in lista:
    print(i)