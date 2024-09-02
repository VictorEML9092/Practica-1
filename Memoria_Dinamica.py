Calificacion = []
max_size = 5

for i in range(5):
    X = int(input("Ingrese un número: "))
    Calificacion.append(X)

if len(Calificacion) > 2:
        Calificacion.pop(2)

print("Las calificaciones son: ",Calificacion)