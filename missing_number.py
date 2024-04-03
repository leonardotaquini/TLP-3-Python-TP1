# Ejercicio 2: “Missing Number”

def missing_number(n, array):
    return sum(range(1, n + 1)) - sum(array)

assert missing_number(5, [1, 3, 4, 5]) == 2, "Error en el caso de prueba"