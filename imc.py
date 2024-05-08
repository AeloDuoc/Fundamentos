import os

# ------------------- VARIABLES -------------------
nombre = ""            # Nombre del usuario
peso = 0                # Peso en kilogramos
estatura = 0            # Estatura en metros
imc = 0                 # IMC calculado
clasificacion =""       # Clasificación según peso
# ----------------- FIN VARIABLES -----------------

nombre = str(input("Ingrese nombre: "))
peso = int(input("Ingrese su peso en kilos: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso/estatura**2
if imc<18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= imc <= 24.9:
    clasificacion = "Peso normal"
elif 25 <= imc <= 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"
    
os.system("cls")    
# ------------------ TICKET ------------------
print(f'''
       ---------------- TICKET ---------------
       Nombre: {nombre}
       Peso: {peso}
       Estatura: {estatura}
       IMC: {round(imc,1)}
       Clasificacion: {clasificacion}
       ''')

# Vamos a esperar tecla
os.system("pause")