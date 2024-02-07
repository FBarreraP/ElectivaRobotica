import numpy

def data(notas, n):
    #global grades
    for i in range(0,n,1):
        n = float(input(f'Ingrese la nota {i+1}: '))
        notas.append(n)
    calificaciones = numpy.array(notas)
    calificaciones = calificaciones + 0.5
    return calificaciones

def average(notas, n):
    s = 0.0
    for i in range(0,n,1):
        s += notas[i]
    a = s/len(notas)
    return s,a

grades = []
grades = data(grades, 5)
r1,r2 = average(grades, 5)
print(f'La suma y el promedio de las notas son: {r1:.2f} y {r2:.2f}')