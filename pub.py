# Programa PUB
import os

# ================== VARIABLES ==================
opcion_menu = "0"       # Opción de menú
producto =""            # Nombre de bebestible
precio = 0              # Precio del bebestible  
cantidad = 0            # Cantidad de bebestible
happy = "N"              # S/N
total = 0               # Total de la compra
mensaje = ""            # Mensaje 

#PROCESO
# =============== MENU =============== 
print('''
      MENU
      N°        PRODUCTO        PRECIO
      1         Vodka tónica    $5.500
      2         Ron cola        $5.000
      3         Cerveza         $2.000
      4         Bebida          $1.500
      ''')
opcion_menu = str(input("Elija su bebida "))
cantidad = int(input("¿Qué cantidad desea? "))
happy = str(input("¿Es Happy Hour (S/N)? ")).upper()

if opcion_menu == "1":
    producto = "Vodka tónica"
    precio = 5500
elif opcion_menu == "2":
    producto = "Ron cola"
    precio = 5000
elif opcion_menu == "3":
    producto = "Cerveza"
    precio = 2000
else:
    producto = "Bebida"
    precio = 1500


# ================TICKET ================
os.system("cls")

if happy=="S":
    total = (precio * cantidad) /2
    mensaje = "<<Compra con descuento>>"
else:
    total = precio * cantidad
    mensaje = "<<No hay descuento T-T>>"
    
print(f'''
      ==================== TICKET ====================
      Tipo de producto: {producto}
      Cantidad: {cantidad}
      Total: $ {total}
      {mensaje}
      ''')

print('''
      ¡Gracias por preferirnos''')    
os.system("pause")