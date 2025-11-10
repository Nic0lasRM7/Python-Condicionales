b = float(input("Ingrese a como su primer valor"))
a = float(input("Ingrese a como su segundo valor"))
c = float(input("Ingrese a como su tercer valor"))

Discriminante = b**2 - (4*a*c)

if a == 0:
   print("No es una ecuacuion cuadratica, a no puede ser igual a 0")
elif Discriminante >= 0:
   print("La ecuacion tiene solucion real")
else:
   print("La ecuacion no tiene una solucion real")
   
          
          