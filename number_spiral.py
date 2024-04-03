# Ejercicio 3: “Number Spiral”

def number_spiral(row, column):
    if row == column:
        print(row**2 - row + 1)
        return row**2 - row + 1
    if row > column:
        if row % 2 == 0:
            print(row**2 - column + 1)
            return row**2 - column + 1
        else:
            print((row - 1)**2 + column)
            return (row - 1)**2 + column
    else: 
        if column % 2 == 0:
            print((column - 1)**2 + row)
            return (column - 1)**2 + row
        else:
            print(column**2 + 1 - row)
            return column**2 + 1 - row
        
assert number_spiral(2, 2) == 3, "Error en el caso de prueba"