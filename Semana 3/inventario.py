from datetime import datetime

producto = input("Ingrese le nombre de producto: ")   #texto
precio = float(input("Ingrese el precio: "))   #decimales
cantidad = int(input("Ingrese la cantidad de productos: "))
#fecha_ingreso = datetime.strptime("2025-02-26", 'd/%m/%Y')
fecha_ingreso = "2025-02-26"

print("-"*40)
print("------Sistema de Facturacion Electronica----")
print(f"Cedula: 12345970")
print(f"Cliente: Luis Llerena")
print(f"Direccion: ambato")
print(f"Telefono: 3216548979")
print(f"Fecha de Venta: {fecha_ingreso}")

print("-"*40)
print("| Cantidad | Producto | Precio | Valor |")
print("-"*40)
print(f"| {cantidad}       | {producto}     | {precio}         | {precio * cantidad} |")
print("-"*40)
print(f"| Sub Total                   | {precio * cantidad} |")
print(f"| IVA                         | {round((precio * cantidad)*0.15,2)} |")
print(f"| TOTAL                       | {round((precio * cantidad)*1.15,2)} |")
