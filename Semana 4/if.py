#estructuras de control   if

#numero = int(input("Ingese un numero y puebe su suerte: "))

#if numero == 5:
#    print("ganador")
#else:
#    print("el perdedor")


    #     ==     igualdad
    #      !=    diferente
    #      >      mayor
    #       <       menor
    #       >=      mayor igual
    #       <=      menor igual 
#--------------------------------------------------------------------------------
#Ejercicio: Clasificación de Edades
#Escribe un programa en Python que solicite al usuario 
#su edad y determine en qué categoría se encuentra según la siguiente tabla:

#Menor de 12 años → "Eres un niño/a."
#Entre 12 y 17 años → "Eres un adolescente."
#Entre 18 y 64 años → "Eres un adulto."
#65 años o más → "Eres un adulto mayor."

#edad = int(input("Ingrese su edad: "))
#if edad < 12:
#    print("Eres un niño/a.")  # verdadero
#elif edad >= 12 and edad <= 17:
#    print("Eres un adolescente.")  # verdadero
#elif edad >=18 and edad <= 64:
#     print("Eres un adulto.")  # verdadero.
#elif edad >= 64:
#    print("Eres un adulto mayor.")  # falso.
#------------------------------------------------------------

#Escribe un programa en Python que solicite al usuario
#ingresar un número y determine si es positivo, negativo o cero.
#Condiciones:
#Si el número es mayor que 0, mostrar: "El número es positivo."
#Si el número es menor que 0, mostrar: "El número es negativo."
#Si el número es exactamente 0, mostrar: "El número es cero."

#numero = int(input("Ingrese un numero: "))
#if numero > 0:
#     print("El numero ingresado es positivo")
#elif numero < 0:
#    print("El numero ingresado es negativo")
#else:
#    print("El numero ingresado es igual a cero")
#----------------------------------------------------------------------
#Escribe un programa en Python que solicite al usuario 
#ingresar una contraseña y verifique si coincide con una 
#contraseña predefinida.

#Condiciones:
#Si la contraseña ingresada es correcta, mostrar: "Acceso concedido."
#Si la contraseña es incorrecta, mostrar: "Acceso denegado."

#contrasenia = input("Ingese su contrasenia: ")

#if contrasenia == "123ABC":
#    print("Acceso concedido")
#else:
#    print("Acceso denegado")

#---------------------------------------------------------------------------
### **Ejercicio: Verificación de acceso con intentos limitados**  

#Escribe un programa en Python que solicite al usuario ingresar
#una contraseña y verifique si coincide con una contraseña predefinida.  

#### **Condiciones:**  
#- Si la contraseña ingresada es correcta, mostrar: `"Acceso concedido."` 
# y finalizar el programa.  
#- Si la contraseña es incorrecta, permitir hasta **tres intentos** 
# antes de bloquear el acceso con el mensaje: `"Acceso bloqueado por 
# intentos fallidos."`  
#- Mostrar el número de intentos restantes después de cada intento fallido.


#contador = 3
#while True:
#    contrasenia = input("Ingese su contrasenia: ")
#    if contador == 0:
#        print("Acceso bloqueado por intentos fallidos")
#        print("Programa Terminado")
#        break 

#    if contrasenia == "123ABC":
#        print("Acceso concedido")
#        break
#    else:
#        contador = contador - 1
#        print(f"Acceso denegado. Numero de intento restante {contador}")
        

#Promedio de notas
#3 calificaciones, necesitamos saber el promedio de las calificaciones
#ingresadas

#Condiciones:
#90 - 100 → "Excelente"
#80 - 89 → "Muy bueno"
#70 - 79 → "Bueno"
#60 - 69 → "Regular"
#Menos de 60 → "Reprobado"

n1 = int(input("Ingese la primera nota: "))        
n2 = int(input("Ingese la segunda nota: "))        
n3 = int(input("Ingese la tercera nota: "))      
promedio = (n1+n2+n3)/3
if promedio > 90 :
    print("Excelente")
elif promedio >= 80 and promedio <= 89:
    print("Muy bueno")
elif promedio >= 70 and promedio <= 79:
    print("Bueno")
elif promedio >= 60 and promedio <= 69:
    print("Regular")
elif promedio < 60:
    print("Reprobado")
