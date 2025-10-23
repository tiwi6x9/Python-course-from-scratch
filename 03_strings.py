                                                             ## String ##
                                                             
## Como definir un string en una varibale y usarlos con ciertas funciones

my_string = 'my_string'
my_other_string = 'my_other_string'

print(len(my_string))
print(len(my_other_string))

print (my_string + '' + my_other_string)

## usar strings con parametros de texto 

my_new_line_string = 'Este es un string \ncon  un salto de linea'
print(my_new_line_string)

my_tab_string = '\tEste es un string con tabulacion'
print(my_tab_string)

my_scape_string = '\tEste es un string \nescapado'
print(my_scape_string)



## Formateo 

## dos maneras de optimizar codigo 

name, surname, age = 'eddison', 'guillermo', 5

print ('mi nombre es' + ' ', name + ' ', surname + ' ' + 'y mi edad es:', age) ## codigo extenso 


# fromas de optimizar 

print('Mi nombre es {} {} y mi edad es {}'.format(name, surname, age)) 

print('Mi nombre es %s %s y mi edad es %s' %(name, surname, age) ) 

print (f'mi nombre es {name}  {surname} y mi edad es {age}')


## Desempaquetado de caracteres 

lenguaje = 'python'

a,b,c,d,e,f = lenguaje

print (a)

print (b)


## Division 

lenguaje_slice = lenguaje[1:3]

print (lenguaje_slice)


## reverse 

reversed_lenguaje = lenguaje[::-1 ]

print ( reversed_lenguaje)


## Funciones 

print (lenguaje.capitalize()) # primera letra en mayuscula 

print (lenguaje.upper()) # todas en mayuscula 

print (lenguaje.count('t')) # para contar cuantas letra del tipo ingresado hay 

print ('1'.isnumeric())
print (lenguaje.isnumeric())

print (lenguaje.lower()) # todas en minuscula 

print (lenguaje.upper().isupper())






