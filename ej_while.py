# El ciclo whihle lleva la siguiente lógica
# MIENTRAS la condición sea VERDADERA seguirá
# iterando (repitiendo), cuando pase a FALSO
# se detiene el ciclo

k = 5

while k <= 10:
    print(k, end=" ")
    k = k+1
    
print("\n\n --- los 1000 primeros naturales")
k = 1
while k <= 1000:
    print(k, end=" ")
    k = k+1

print("\n\n --- los 500 primeros impares ---")
k = 1
while k <= 500:
    print(f"{k*2-1}", end=" ")
    k = k+1