 # Variables 
 

 # Paso para generar una variable, le damos un type(tipo de valor) e imprimimos nuestra variable
 
my_variable = 'My string variable'

print ( my_variable) 

# asignamos otro tipo de valor a nuestra variable (type)

my_int_variable = 5

print ( my_int_variable) 

# asignamos otro tipo de valor a nuestra variable (type) bool

my_bool_variable = True

print ( my_bool_variable) 



#usar el pirnt para imprimir diferentes argumentos/ variables mediante el uso de comas en cadena

# Concatenacion de variables en un print 
print (my_bool_variable, my_int_variable, my_variable)

#  Convertir un tipo de dato e identificarlo 

# primero definimos el tipo de dato en este caso float
my_float_variable = 1.5
print(my_float_variable)

# transformamos a tipo de dato string mediante el str y la consola nos va a devover que nuestra variable sera string mas no float
my_float_to_string_variable = str(my_float_variable)
print(my_float_variable)
print(type(my_float_to_string_variable))


# Algunas Funciones de Sistema 
# len () sirve para contar en este ejemplo cuantas letras tiene esta string 

my_string_variable = 'my string variable'

print(len(my_string_variable))



# algunos ejemplos de concatenacion de variables mediante comas

print ('El valor es:', my_bool_variable)


# Variables en una sola linea. !Cuidado con el abuso de esta sintaxis!

name, surname, alias, age = 'Eddison', "Guillermo", 'tiwi', 25

print('mi nombre es:', name, surname, 'Tengo ', age, 'anos', 'y mi alias es',  alias)


# Funcion - input() sirve para capturar datos mediante consola

first_name = input('Ingrese su nombre:')
last_name = input ('Ingrese su apellido:')

print(first_name)
print(last_name)

# Ejemplo de como cambiar el tipo a una variable 

first_name = 25
last_name = 'tiwi'

print(first_name)
print(last_name)


# Forzamos el tipo 

address: str = 'mi direccion'

address = 32 

print(type(address))









