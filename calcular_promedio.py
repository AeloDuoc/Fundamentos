import os

# Declarar variables
nota_1 = 0
nota_2 = 0
nota_3 = 0
promedio = 0
op_menu = ""
while op_menu!="3":
    print ('''
    --- MENU ---
    1.- Calcular promedio
    2.- Ver resultados estadísticas
    3.- Salir
    ''')
    op_menu = str(input("Elija una opción: "))
    if op_menu == "1":
        #Manejo de excepciones
        #Nota 1
        while True:
            try:
                nota_1 = float(input("Ingrese nota 1: "))
                while not 1<= nota_1 <= 7:
                    os.system("cls")
                    print("Error. rango de 1 a 7")
                    nota_1 = float(input("Ingrese nota 1: "))
                break
            except:
                print("Error, ingreso de dato erróneo")
        #Nota 2
        while True:
            try:
                nota_2 = float(input("Ingrese nota 2: "))
                while not 2<= nota_1 <= 7:
                    os.system("cls")
                    print("Error. rango de 1 a 7")
                    nota_2 = float(input("Ingrese nota 2: "))
                break
            except:
                print("Error, ingreso de dato erróneo")
        #Nota 3
        while True:
            try:
                nota_3 = float(input("Ingrese nota 3: "))
                while not 2<= nota_3 <= 7:
                    os.system("cls")
                    print("Error. rango de 1 a 7")
                    nota_3 = float(input("Ingrese nota 3: "))
                break
            except:
                print("Error, ingreso de dato erróneo")
    
    if op_menu == "2":
        os.system("cls")
        promedio = (nota_1 + nota_2 + nota_3)/3
        print(f'''Promedio: {promedio}
        ''')
        
    if op_menu == "3":
        os.system("cls")
        print("Gracias por el sistema. Adiós")     
          
               
    os.system("pause")