import config
import main
import render
def crear_tablero_minas():
    tablero = []
    for i in range(config.LARGO_TABLERO):
        tablero.append([])
    for fila in tablero:
        for i in range(config.LARGO_TABLERO):
            fila.append(0)
    return tablero
#print(crear_tablero_minas())

def crear_tablero_revelado():
    tablero = []
    for i in range(config.LARGO_TABLERO):
        tablero.append([])
    for fila in tablero:
        for i in range(config.LARGO_TABLERO):
            fila.append(False)
    return tablero
#print(crear_tablero_revelado())

tablero_de_prueba = crear_tablero_minas()

print('[')
for row in tablero_de_prueba:
    print(row)
print(']')

tablero_de_prueba = main.plantar_bombas(tablero_de_prueba)

print('-----')
print('[')
for row in tablero_de_prueba:
    print(row)
print(']')

tablero_de_prueba = main.calcular_adyacentes(tablero_de_prueba)
print('[')
for row in tablero_de_prueba:
    print(row)
print(']')
