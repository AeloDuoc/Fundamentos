import os
import time

# =================== VARIABLES ===================
opcion_menu = ""        # opción de producto
nombre_producto = ""    # nombre de producto
cantidad = 0            # cantidad
valor_producto = 0      # valor unitario
es_mayorista = False    # es o no compra mayorista
descuento = 0           # monto del descuento
en_efectivo = "N"       # S/N
total_pagar = 0         # total de la compra

# =============== CÓDIGO PRINCIPAL ===============

# Menú
while opcion_menu!="4":
    print ('''
================= MENÚ =================
PRODUCTO                 VALOR UNITARIO
1.- Tazón                $  500
2.- Llavero              $  200
3.- Polera estampada     $3.000
''')

    opcion_menu = str(input("Elija un producto: "))
    os.system("pause")
    if opcion_menu == "1":
        nombre_producto = "Tazón"
        valor_producto = 500
        break
    elif opcion_menu == "2":
        nombre_producto = "Llavero"
        valor_producto = 200
        break
    else:
        nombre_producto = "Polera estampada"
        valor_producto = 3000
        break
    os.system("cls")

    while cantidad == 0:
        cantidad= int(input("¿Qué cantidad desea? "))

    en_efectivo = str(input("¿Pagará en efectivo? (S/N) ")).upper()
    if cantidad >= 100 and opcion_menu = 1:
        valor_producto = 300
        es_mayorista = True
    elif cantidad >= 300 and opcion_menu = 2:
        valor_producto = 150
        es_mayorista = True
    elif cantidad >= 50 and opcion_menu = 3
        valor_producto = 2000
        es_mayorista = True
    
    
    if en_efectivo == "S" and es_mayorista:
        total_pagar = valor_producto * cantidad * 0.9
    else:
        total_pagar = valor_producto * cantidad        
        
    

        
    os.system("pause")
    


