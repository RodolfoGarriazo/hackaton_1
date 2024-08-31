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
if _name_ == "_main_":
    # Pruebas
    assert suma(10, 5) == 15, "Error en suma(10, 5)"
    assert suma(-3, 3) == 0, "Error en suma(-3, 3)"
    assert suma(0, 0) == 0, "Error en suma(0, 0)"
    assert suma(1.5, 2.5) == 4.0, "Error en suma(1.5, 2.5)"
    
    # Mostrar resultados
    print("Todas las pruebas pasaron para la función suma.")