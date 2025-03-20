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

"""
    Calculo de niveles de embriones en el juego de Reapers
    r = Nivel de la Reaper
    p = Nivel de tu personaje
    e = Nivel del embrion sin sumar los 75 puntos base.
    final_level = Nivel final del embrion despues de la suma de los 75 puntos base.
"""
def calculate_level(r, p):
    if r < 0 or p < 0:
        raise ValueError("Los niveles no pueden ser negativos.")
    e = r * (p + 100) / 250
    return int(e + 75) 

"""
    Función de la lista de equivalencias de 100 tek.
    quantity_tek = Cantidad de tek a convertir.
    convertion = Diccionario de la equivalencia de 100 tek.
    en la interacion se multiplica la cantidad de tek por el valor de la equivalencia (value) y se redondea.
"""
def convertion_tek(quantity_tek):
    if quantity_tek < 0:
        raise ValueError("La cantidad de tek no puede ser negativa.")
    result = {}
    for item, value in convertion.items():
        result[item] = round((quantity_tek / 100) * value)  
    return result
