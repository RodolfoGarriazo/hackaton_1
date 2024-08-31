# resta.py

def resta(a, b):
    """
    Función que realiza la resta de dos números.

    Parámetros:
    a (float): Minuendo (el número del que se va a restar).
    b (float): Sustraendo (el número que se va a restar).

    Retorna:
    float: El resultado de la resta de 'a' menos 'b'.
    """
    return a - b
#suma  
def suma(a, b):
    """
    Función que realiza la suma de dos números.

    Parámetros:
    a (float): Primer número.
    b (float): Segundo número.

    Retorna:
    float: El resultado de la suma de 'a' más 'b'.
    """
    return a + b  

# Ejemplo de uso y pruebas
if __name__ == "__main__":
    # Pruebas
    assert resta(10, 5) == 5, "Error en resta(10, 5)"
    assert resta(-3, -3) == 0, "Error en resta(-3, -3)"
    assert resta(0, 0) == 0, "Error en resta(0, 0)"
    assert resta(1.5, 0.5) == 1.0, "Error en resta(1.5, 0.5)"
    
    # Mostrar resultados
    print("Todas las pruebas pasaron para la función resta.")
    
    assert suma(10, 5) == 15, "Error en suma(10, 5)"
    assert suma(-3, 3) == 0, "Error en suma(-3, 3)"
    assert suma(0, 0) == 0, "Error en suma(0, 0)"
    assert suma(1.5, 2.5) == 4.0, "Error en suma(1.5, 2.5)"
    
    # Mostrar resultados
    print("Todas las pruebas pasaron para la función suma.")



# Ejemplo de uso
