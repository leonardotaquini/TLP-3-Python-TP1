# Ejercicio 1: “Weird Algorithm”

def weird_algorithm(n):
    num_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            num_list.append(n)
        else:
            n = n * 3 + 1
            num_list.append(n)
    return num_list

assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"