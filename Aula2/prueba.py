def data():
    global grades
    for i in range(0,5,1):
        n = float(input('Ingrese la nota '+str(i+1)+" : \n"))
        grades.append(n)

def average(notas):
    s = 0.0
    for i in range(0,5,1):
        s += notas[i]
    a = s/len(notas)
    return s,a

grades = []
data()
r1,r2 = average(grades)
print('La suma y el promedio de las notas son: %.2f y %.2f' %(r1,r2))
