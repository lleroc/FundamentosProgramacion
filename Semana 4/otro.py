### **Ejercicio: Sistema de evaluación de empleados**  

#Escribe un programa en Python que solicite al usuario ingresar 
# la puntuación de un empleado (de 0 a 100) y determine su nivel
#  de desempeño y bonificación según la siguiente escala:  

#### Condiciones:
#- 90 - 100 → `"Desempeño excelente"` → Bonificación del 30% sobre el salario.  
#- 80 - 89 → `"Desempeño muy bueno"` → Bonificación del 20% sobre el salario.  
#- 70 - 79 → `"Desempeño bueno"` → Bonificación del 10% sobre el salario.  
#- 60 - 69 → `"Desempeño regular"` → No hay bonificación.  
#- Menos de 60 → `"Desempeño insuficiente"` → Advertencia de bajo rendimiento.  
#- Si la puntuación está fuera del rango, mostrar `"Puntuación no válida."`  

#Además, el programa debe solicitar el salario base del empleado 
# y calcular la bonificación correspondiente.

nombre = input("Ingrese su nombre= ")
puntuacion = int(input("Ingrese la puntuacion= "))
salario = float(input("Ingrese el salario= "))
if puntuacion >= 90 and puntuacion <= 100:
    print(f"{nombre} => Desempeño excelente. Bonificacion del 30% sobe el salario")
    print(salario * 1.3)
    bonificacion = salario * 0.3
    total = salario + bonificacion
    print(f"calculo del total paso a paso. Resultaddo = {total}")
elif puntuacion >= 80 and puntuacion <= 89:
    print(f"{nombre} => Desempeño muy bueno. Bonificacion del 20% sobe el salario")
    print(salario * 1.2)
elif puntuacion >= 70 and puntuacion <= 79:
    print(f"{nombre} => Desempeño bueno. Bonificacion del 10% sobe el salario")
    print(salario * 1.1)
elif puntuacion >= 60 and puntuacion <= 69:
    print(f"{nombre} => Desempeño regular. No hay bonificación.")
elif puntuacion <60:
    print(f"{nombre} => Desempeño insuficiente. Advertencia de bajo rendimiento")
else:
    print("Puntuacion fuera de rango")


