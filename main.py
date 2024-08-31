# multiplicacion.py

def multiplicacion(a, b):
    """
    Función que realiza la multiplicación de dos números.

    Parámetros:
    a (float): Primer número.
    b (float): Segundo número.

    Retorna:
    float: El resultado de la multiplicación de 'a' por 'b'.
    """
    return a * b

# Ejemplo de uso y pruebas
if _name_ == "_main_":
    # Pruebas
    assert multiplicacion(10, 5) == 50, "Error en multiplicacion(10, 5)"
    assert multiplicacion(-3, 3) == -9, "Error en multiplicacion(-3, 3)"
    assert multiplicacion(0, 0) == 0, "Error en multiplicacion(0, 0)"
    assert multiplicacion(1.5, 2.0) == 3.0, "Error en multiplicacion(1.5, 2.0)"
    
    # Mostrar resultados
    print("Todas las pruebas pasaron para la función multiplicacion.")