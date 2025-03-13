#Lista de la equivalencia de 100 tek.
convertion = {
        'Tek Celling': 100,
        'Tek Wall': 120,
        'Tek Pillar': 200,
        'Tek Large Walls': 30,
        'Tek Roof/Ramp/Stairs': 100,
        'Tek Sloped Walls': 350,
        'Tek Foundation': 80,
        'Tek Triangle Fundation': 200,
        'Tek Vaccum Compartments': 20,
        'Tek Generator': 3,
        'Tek Replicator': 1,
        'Tek Cloning Chamber': 1,
        'Tek Dedicated Storage': 30,
        'Tek Transmiter': 3,
        'Tek Trough': 5,
        'Tek Triangle Ceiling': 200,
        'Medium TP': 4,
        'Hard Poly': 10000,
        'Black Perls': 1000,
        'Metal Lingots': 20000,
        'Crystal': 40000
    }

#Funcion para calcular niveles de embriones en el juego Reapers
def calculate_level(r, p):
    e = r * (p + 100) / 250
    final_level = int(e + 75)
    return final_level

#Funcion para la conversion tek de los items de de la lista.
def convertion_tek(quantity_tek):
    print(f'\nEquivalencias para {quantity_tek} Tek:\n')
    for item, value in convertion.items():
        quantity_convertion = round((quantity_tek / 100) * value)
        print(f'- {item} = {quantity_convertion}')

while True:
    print('\nBienvenido a la calculadora de niveles de Reapers y Conversion Tek.')
    print('\n1.- Calcular nivel de embrion.')
    print('2.- Conversion Tek.')
    print('3.- Salir.')

    option = input('\nSeleccione una opción: ')

    if option == '1':
        try:
            r = int(input('1.- Nivel del Reaper: '))
            p = int(input('2.- Nivel del Personaje: '))

            if r < 0 or p < 0:
                print('Los valores deben ser positivos. Inténtelo de nuevo.')
                continue

            level_baby = calculate_level(r, p)
            print(f'\nEl nivel del embrion es: {level_baby}')
            break

        except ValueError:
            print('Error de parametros: Ingrese solo número enteros')
    
    elif option == '2':
        try:
            quantity_tek = int(input('Ingrese la cantidad de Tek: '))

            if quantity_tek < 0:
                print('\nEl valor debe ser positivo. Inténtelo de nuevo.')
                continue

            convertion_tek(quantity_tek)
            break

        except ValueError:
            print('Error de parametros: Ingrese un número valido')

    elif option == '3':
        print('Saliendo del programa...')
        break

    else:
        print('Opción no valida. Inténtelo de nuevo.')
