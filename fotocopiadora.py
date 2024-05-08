# Hojas valen 20 si hay más de 30 10% de descuento
import os
os.system("cls")  

hojas = int(input("Indique cantidad de hojas: "))

if hojas > 30:
    precio = 20 * hojas * 0.9
else:
    precio = 20 * hojas

os.system("cls")    
print(f'''
    ========== TICKET ==========
    Total hojas: {hojas}
    Precio a pagar: $ {round(precio)}
    ¡Gracias por preferirnos!
    ============================
    ''')