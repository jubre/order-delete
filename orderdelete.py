#!/usr/bin/env python3

# Funcion que Ordena y Elimina los duplicados
def ordered_set(in_list):
    out_list = []
    added = set()
    for val in in_list:
        if not val in added:
            out_list.append(val)
            added.add(val)
    out_list.sort()
    return out_list

# Funcion principal: captura los datos
def run():
    # myList = [10,8,1,1,3,6,2]
    # print(myList)
    # print(ordered_set(myList))

    input = str(raw_input('Ingresa los datos, separado por espacios: ')).split()

    input = list(map(int, input))

    print(ordered_set(input))

# Nuestro programa empieza aqui.
if __name__ == '__main__':
	run()
