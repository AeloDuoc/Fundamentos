# Vamos a capturar datos desde el usuario

import os
# Limpiar pantalla
os.system("cls")

nombre = str(input("Ingrese nombre: "))

edad = int(input("Ingrese edad: "))
nota_1 = float(input("Ingrese nota 1: "))
nota_2 = float(input("Ingrese nota 2: "))
nota_3 = float(input("Ingrese nota 3: "))

promedio = round((nota_1 + nota_2 + nota_3)/3,1)

if promedio >= 4:
    estado = "APROBADO"
else:
    estado = "REPROBADO"

os.system("cls")    
print(f'''
    ========== TICKET ==========
    Nombre: {nombre}
    Edad: {edad}
    Nota 1: {nota_1}
    Nota 2: {nota_2}
    Nota 3: {nota_3}
    Promedio: {promedio}
    Estado: {estado}  
    ''')
    