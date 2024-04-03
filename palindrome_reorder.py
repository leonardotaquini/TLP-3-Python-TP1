from itertools import permutations

def is_palindrome(cadena):
    return cadena == cadena[::-1]

def palindrome_reorder(cadena):
    # Genero todas las combinaciones de la cadena
    todas_permutaciones = permutations(cadena)
  
    lista_palindromos = []

    # Verifico si alguna de las combinaciones es un palíndromo y lo agrego a una lista
    for perm in todas_permutaciones:
        if is_palindrome(perm):
            lista_palindromos.append(''.join(perm))
    return lista_palindromos



# Ejemplo de uso y prueba del assert
assert ('bacab' in palindrome_reorder("aabbc")), "Error en el caso de prueba"