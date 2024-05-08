# range es un rango
# range(n) va desde cerp a n-1
# Ej- range(3)--> (0,1,2)

for k in range(5):
    print(k)

print("\n\n --- también se imprime horizontal")
for j in range(10):
    print(j, end=", ")

print(f"\n\n --- range(2,15) ---")
for k in range(2,15):
    print(k, end=", ")
    
print(f"\n\n--- range(2,15,2---)")    
for k in range(2,15,2):
    print(k, end=", ")
    
print(f"\n\n --- range(100,10, -5) ---")
for k in range(100,10,-5):
    print(k, end=", ")
    
# Propuesto 1
# Imprimir primeros 1000 números naturales
# 1,2,3,4--- 1000

print("\n\n Primeros 1000")
for k in range(1,1001):
    print(k, end=", ")

# Propuesto 2
# Imprimir los 100 impares
# 1,3, 5

print ("\n\n Impares")
for k in range(1,101):
    print(2*k-1, end=", ")
    
# Prpuesto 5000 primeros pares
print("\n\n 5000 pares")
for k in range(1,5001):
    print(2*k, end =", ")