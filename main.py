# division.py

def division(a, b):
    """
    Función que realiza la división de dos números.

    Parámetros:
    a (float): Dividendo (el número que se va a dividir).
    b (float): Divisor (el número por el que se va a dividir).

    Retorna:
    float: El resultado de la división de 'a' entre 'b', o None si b es cero.
    """
    if b == 0:
        print("Error: No se puede dividir por cero.")
        return None
    return a / b

# Ejemplo de uso y pruebas
if _name_ == "_main_":
    # Pruebas
    assert division(10, 5) == 2.0, "Error en division(10, 5)"
    assert division(-9, 3) == -3.0, "Error en division(-9, 3)"
    assert division(0, 1) == 0.0, "Error en division(0, 1)"
    assert division(1.5, 0.5) == 3.0, "Error en division(1.5, 0.5)"
    assert division(1, 0) is None, "Error en division(1, 0)"  # Prueba para la división por cero
    
    # Mostrar resultados
    print("Todas las pruebas pasaron para la función division.")