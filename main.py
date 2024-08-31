
# multiplicacion.py

def multiplicacion(a, b):
  
    """
    Función que realiza la multiplicación de dos números.

    float: El resultado de la multiplicación de 'a' por 'b'
    """
    return a * b

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
     >>>>>>> main
     """"
    """
    Parámetros:
    a (float): Primer número.
    b (float): Segundo número.
    """
    "" El resultado de la suma de 'a' más 'b'.""
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
    
    assert division(10, 5) == 2.0, "Error en division(10, 5)"
    assert division(-9, 3) == -3.0, "Error en division(-9, 3)"
    assert division(0, 1) == 0.0, "Error en division(0, 1)"
    assert division(1.5, 0.5) == 3.0, "Error en division(1.5, 0.5)"
    assert division(1, 0) is None, "Error en division(1, 0)"  # Prueba para la división por cero
    
    # Mostrar resultados
    print("Todas las pruebas pasaron para la función division.")
    
    assert multiplicacion(10, 5) == 50, "Error en multiplicacion(10, 5)"
    assert multiplicacion(-3, 3) == -9, "Error en multiplicacion(-3, 3)"
    assert multiplicacion(0, 0) == 0, "Error en multiplicacion(0, 0)"
    assert multiplicacion(1.5, 2.0) == 3.0, "Error en multiplicacion(1.5, 2.0)"
    
    # Mostrar resultados
    print("Todas las pruebas pasaron para la función multiplicacion.")



