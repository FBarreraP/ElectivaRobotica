class Estudiante():
    #constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
        self.ocupacion = "Estudiante"
        self.grades = []
        self.s = 0.0
        self.a = 0
        
    #atributos
    
    #métodos        
    def data(self, x):
        for i in range(0,x,1):
            n = float(input('Ingrese la nota '+str(i+1)+" : "))
            self.grades.append(n)

    def average(self, x):
        for i in range(0,x,1):
            self.s += self.grades[i]
        self.a = self.s/len(self.grades)
        return self.s,self.a
    
    def result(self):
        print('La suma y el promedio de las notas son: %.2f y %.2f' %(self.s,self.a))
    
Fabian = Estudiante('Fabián',20) #instancia
Fabian.data(5)
r1,r2 = Fabian.average(5)
print('La suma y el promedio de las notas son: %.2f y %.2f' %(r1,r2))
Fabian.result()