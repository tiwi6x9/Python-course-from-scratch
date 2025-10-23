# ============================================
# CLASE 02 - OPERADORES EN PYTHON
# ============================================

# ============================================
# 🔹 OPERADORES ARITMÉTICOS
# ============================================

# Sirven para realizar operaciones matemáticas básicas
print(3 + 2)   # Suma → 5
print(3 - 2)   # Resta → 1
print(3 * 2)   # Multiplicación → 6
print(3 / 2)   # División → 1.5
print(10 % 2)  # Módulo → resto de la división (10 ÷ 2 = 5, resto = 0)
print(10 // 3) # División entera → 3 (descarta los decimales)
print(2 ** 3)  # Potencia → 2³ = 8
print(5 + 5 - 2 * 7)  # Orden de operaciones: 5 + 5 - (2 * 7) = -4

# --------------------------------------------
# Operaciones con cadenas (strings)
# --------------------------------------------
print('Hola' + ' Python')  # Concatenación de texto
print('Hola' + str(5))     # Convertimos número a string para unirlo
print('Hola' * 2)          # Repite la cadena dos veces

# Transformar float a entero para usarlo en una operación de texto
my_float = (2.5 * 2)
print('Hola' * int(my_float))  # int(5.0) → 5 → 'Hola' * 5


# ============================================
# 🔹 OPERADORES COMPARATIVOS
# ============================================

# Devuelven True o False según la comparación
print(3 < 4)   # True
print(3 > 4)   # False
print(3 <= 4)  # True
print(3 >= 4)  # False
print(3 == 4)  # False (igualdad)
print(3 != 4)  # True (diferente)
print(3 < 4 == 2)  # Evaluación encadenada → False

# Comparaciones entre cadenas (orden alfabético)
print('Hola' < 'Python')  # True (H viene antes que P)
print('Hola' > 'Python')  # False
print('Hola' == 'Zola')   # False


# ============================================
# 🔹 OPERADORES LÓGICOS
# ============================================

# Trabajan con valores booleanos (True/False)
# AND → Todas las condiciones deben ser verdaderas
# OR → Al menos una condición debe ser verdadera
# NOT → Niega (invierte) el valor booleano

print(3 > 4 and "Hola" > "Python")  # False and False → False
print(3 > 4 or "Hola" > "Python")   # False or False → False
print(not (3 > 4))                  # not False → True




# ============================================
# EJERCICIO: Mini Calculadora
# ============================================

# Pedimos los datos al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostramos operaciones básicas
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")

# Mostramos comparaciones
print(f"¿El primer número es mayor que el segundo?: {num1 > num2}")
print(f"¿Son iguales?: {num1 == num2}")

# Ejemplo con operador lógico
print(f"¿El primer número es mayor que 0 y menor que 100?: {num1 > 0 and num1 < 100}")
