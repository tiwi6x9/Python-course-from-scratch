                                                                   ###  OPERADORES ARITMETICOS  ###

## OPERADORES BASICOS EN UN PRITN PARA MOSTRAR EL RESULTADO 

print ( 3 + 2)
print ( 3 - 2)
print ( 3 * 2)
print ( 3 / 2)
print (10 % 2) ## operador de modulo 
print(10 // 3) ## floordivision // divison estrictamente con un resultado de nuemro entero aproximado 
print (2 ** 3) ## sirve para calcular el elevado de un numero 
print (5 + 5 - 2 * 7) 



## Sumar dos cadenas de texto !! Se usa unicamnete con signos especificos no en todos los casos 

print('Hola' + ' Python')
print ( 'Hola'+ str(5)) # manera de llamar a funcion string para concatenar un numero con un string 
print ('Hola' * 2 )

## transformar un numero float a un entero para poder realizar una operacion entre este y un string !! ejercicio de logica !! 

my_float = (2.5 * 2)
print ('hola' * int(my_float))



                                                                ###  OPERADORES COMPARATIVOS  ###


## Estos operadores comparativos sirven para comprar un dato de otro y decir si es verdadero o falso 

print (3 < 4) 
print (3 > 4)
print (3 <= 4)
print (3 >= 4)
print (3 == 4)
print (3 != 4)
print (3 < 4 == 2)


## Comparamos strings // Se compara una ordenacion alfabetica  

print ('Hola' < 'Python') 
print ('Hola' > 'Python')
print ('Hola' == 'Zola') ## Z por muy debajo de H por lo tanto no se cunmple que H sea igual a Z 

 

                                                                ###  OPERADORES LOGICOS  ###
                                                                
 ## Tener en cuenta que aqui entra la logica booleana que va a regir los resultados si cumple o no 
 
 
print (3 > 4 and "Hola" > 'Python') # en stos casos las dos no cumple por lo que son false y "false + false = false"
print (3 > 4 or "Hola" > 'Python')

print (not (3 > 4) ) # Este ultimo operador es para negar el resultado 






 