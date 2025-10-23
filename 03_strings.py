# ============================================
# CLASE 03 - STRINGS EN PYTHON
# ============================================

# Los *strings* (cadenas de texto) son secuencias de caracteres encerradas entre comillas simples o dobles.
# Son uno de los tipos de datos más utilizados en Python.

# ============================================
# 🔹 CREACIÓN Y CONCATENACIÓN DE STRINGS
# ============================================

my_string = "Hola"
my_other_string = 'Python'

# len() devuelve la longitud (número de caracteres) del string
print(len(my_string))          # 4
print(len(my_other_string))    # 6

# Concatenar strings (unir texto)
print(my_string + " " + my_other_string)  # Hola Python

# También se pueden unir varias cadenas
saludo = my_string + " desde " + my_other_string
print(saludo)  # Hola desde Python


# ============================================
# 🔹 CARACTERES ESPECIALES
# ============================================

# \n → salto de línea
# \t → tabulación
# \\ → barra invertida literal

new_line = "Este es un texto\ncon salto de línea"
tab_text = "\tEste texto tiene una tabulación"
scape_text = "Este texto contiene una barra invertida: \\"

print(new_line)
print(tab_text)
print(scape_text)


# ============================================
# 🔹 FORMATEO DE STRINGS
# ============================================

# Existen tres formas principales de insertar variables dentro de un texto:

name, surname, age = "Eddison", "Guillermo", 25

# 1️⃣ Concatenación tradicional
print("Mi nombre es " + name + " " + surname + " y tengo " + str(age) + " años.")

# 2️⃣ Método .format()
print("Mi nombre es {} {} y tengo {} años.".format(name, surname, age))

# 3️⃣ f-Strings (más moderna y recomendada)
print(f"Mi nombre es {name} {surname} y tengo {age} años.")

# Puedes usar expresiones dentro de un f-string
print(f"El próximo año tendré {age + 1} años.")


# ============================================
# 🔹 DESEMPAQUETADO DE CARACTERES
# ============================================

# Se puede asignar cada carácter de un string a variables separadas:
language = "python"

a, b, c, d, e, f = language  # cada letra a una variable
print(a)  # p
print(b)  # y


# ============================================
# 🔹 SLICING (CORTES DE STRING)
# ============================================

# Permite obtener subcadenas indicando posiciones de inicio y fin: [inicio:fin]

print(language[0:3])   # pyt → desde índice 0 hasta 2
print(language[1:4])   # yth → desde índice 1 hasta 3
print(language[:4])    # pyth → desde inicio hasta índice 3
print(language[2:])    # thon → desde índice 2 hasta el final

# También se puede invertir el texto:
print(language[::-1])  # nohtyp


# ============================================
# 🔹 FUNCIONES Y MÉTODOS DE STRINGS
# ============================================

# Los strings tienen muchos métodos útiles para manipular texto

text = "python"

print(text.capitalize())   # Python → primera letra en mayúscula
print(text.upper())        # PYTHON → todo en mayúsculas
print(text.lower())        # python → todo en minúsculas
print(text.count("t"))     # 1 → cuántas veces aparece una letra
print("123".isnumeric())   # True → todos los caracteres son números
print("Hola".isnumeric())  # False
print(text.upper().isupper())  # True → ¿está todo en mayúsculas?
print(text.startswith("p"))    # True → ¿empieza con "p"?
print(text.endswith("n"))      # True → ¿termina con "n"? 


# ============================================
# 🔹 CONCATENACIÓN, REPETICIÓN Y CONVERSIÓN
# ============================================

# Unir texto y números
year = 2025
print("Estamos en el año " + str(year))  # Conversión de int → str

# Repetir un texto varias veces
print("Python! " * 3)  # Python! Python! Python!


# ============================================
# 🔹 STRINGS MULTILÍNEA
# ============================================

# Puedes crear un texto que ocupe varias líneas con triple comillas
multi_text = """Hola,
este es un texto
de varias líneas."""
print(multi_text)


# ============================================
# 🔹 RESUMEN DE FUNCIONES ÚTILES
# ============================================

# len()        → longitud del texto
# .upper()     → mayúsculas
# .lower()     → minúsculas
# .capitalize()→ primera letra mayúscula
# .count()     → contar caracteres
# .isnumeric() → verifica si es numérico
# .startswith() / .endswith() → inicio o fin
# .format() / f"" → formateo moderno
# [::]         → slicing (corte de texto)
#[::-1]        → invertir texto




# ============================================
# EJERCICIO: Presentación personal
# ============================================

# Pedimos los datos al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")

# Creamos un mensaje formateado con salto de línea y mayúsculas
mensaje = f"\nHola, mi nombre es {nombre.capitalize()} {apellido.capitalize()}.\nTengo {edad} años y estoy aprendiendo Python."

# Mostramos el mensaje final
print(mensaje)
