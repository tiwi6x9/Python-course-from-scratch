# ============================================
# CLASE 01 - VARIABLES EN PYTHON
# ============================================

# Una variable es un espacio en memoria donde guardamos un valor
# Python detecta automáticamente el tipo de dato (no es necesario declararlo)

# Asignamos una variable tipo string (cadena de texto)
my_variable = 'My string variable'
print(my_variable)

# Asignamos un número entero (int)
my_int_variable = 5
print(my_int_variable)

# Asignamos un valor booleano (True o False)
my_bool_variable = True
print(my_bool_variable)

# Podemos imprimir varias variables separadas por comas
print(my_bool_variable, my_int_variable, my_variable)

# --------------------------------------------
# Conversión de tipos y funciones básicas
# --------------------------------------------

# Asignamos un número decimal (float)
my_float_variable = 1.5
print(my_float_variable)

# Convertimos un float a string
my_float_to_string_variable = str(my_float_variable)
print(my_float_to_string_variable)
print(type(my_float_to_string_variable))  # Muestra el tipo de dato actual

# La función len() cuenta los caracteres de una cadena
my_string_variable = 'my string variable'
print(len(my_string_variable))  # Devuelve 17

# --------------------------------------------
# Concatenación de variables
# --------------------------------------------
print('El valor es:', my_bool_variable)

# Variables en una sola línea (no recomendado abusar de esto)
name, surname, alias, age = 'Eddison', 'Guillermo', 'tiwi', 25
print('Mi nombre es:', name, surname, ', tengo', age, 'años y mi alias es', alias)

# --------------------------------------------
# Captura de datos por consola
# --------------------------------------------
# La función input() permite ingresar información desde el teclado
first_name = input('Ingrese su nombre: ')
last_name = input('Ingrese su apellido: ')

print('Hola', first_name, last_name)

# --------------------------------------------
# Cambio de tipo en variables
# --------------------------------------------
# Python permite cambiar el tipo de una variable en cualquier momento
first_name = 25
last_name = 'Tiwi'

print(first_name)
print(last_name)

# --------------------------------------------
# Tipado forzado (Type Hints)
# --------------------------------------------
# Podemos sugerir el tipo de dato, aunque Python no lo obliga
address: str = 'Mi dirección'
address = 32  # Python lo permite igualmente
print(address)
print(type(address))\
    



# ============================================
# EJERCICIO: Calculadora de edad futura
# ============================================

# Pedimos los datos al usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad actual: "))

# Calculamos la edad dentro de 10 años
edad_futura = edad + 10

# Mostramos el resultado usando f-strings
print(f"Hola {nombre}, en 10 años tendrás {edad_futura} años.")
