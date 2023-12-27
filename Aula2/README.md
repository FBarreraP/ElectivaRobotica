<h1>Aula 2</h1>

En esta clase se enseña a utilizar repositorio git, `Python` con el Toolbox de Peter Corke e interfaces gráficas (GUIs).

<h2>Repositorio git</h2>

Los repositorios GitHub y GitLab son utilizados principalmente por el terminal, donde los comandos son similares a los de Linux, algunos de dichos comandos son:

```linux
COMANDOS LINUX
ls -> Muestra la lista de archivos en la ruta actual
la -a -> Muestra la lista de archivos incluyendo archivos ocultos en la ruta actual
pwd -> Muestra la ruta actual
cd [FOLDERNAME] -> Entra a una carpeta especificada
cd .. -> Regresa al punto anterior de la ruta
cp [FILETOCOPY] [DESTINATIONFOLDER]-> Copia archivos o carpetas
mv [FILETOMOVE] [DESTINATIONFOLDER]-> Mueve archivos y carpetas
mv [ORIGINALFILE] [RENAMEDFILE]-> Renombra archivos y carpetas
touch [FILE] -> Crea un archivo en la ruta actual
rm [FILE] -> Elimina un archivo
rm -r [FOLDER] -> Elimina una carpeta
mkdir [FOLDERNAME] -> Crea una carpeta en la ruta actual
rmdir [FOLDERNAME] -> Elimina una carpeta en la ruta actual
sudo -> Brinda permisos de administrador (superusuario)
nano -> Abre un archivo específico
```

Inicialmente se debe configurar la identidad de la cuenta para posteriormente realizar la sincronización del repositorio local con el repositorio web, teniendo en cuenta los siguientes comandos:

```git
git config --global user.name “[USERNAME]” (ej: git config --global user.name “FBarreraP”)
git config --global user.email “[USEREMAIL]” (ej: git config --global user.email “fbarrera6@gmail.com”)
```
Para crear un repositorio web a partir de una carpeta local (PC)

```
Entrar a la carpeta a través del terminal teniendo en cuenta los comandos linux anteriormente presentados
git init 
git add README.md 
git commit -m "algun_comentario" 
git branch -M main
git remote add origin https://github.com/FBarreraP/nombre_repositorio_web (ej: https://github.com/FBarreraP/ElectivaRobotica.git)
git push -u origin main 
```

Para crear un repositorio local (PC) desde un repositorio web

```
Entrar a la carpeta a través del terminal teniendo en cuenta los comandos linux anteriormente presentados
git clone https://github.com/FBarreraP/nombre_repositorio_web (ej: https://github.com/FBarreraP/ElectivaRobotica.git)
cd nombre_repositorio_web (ej: ElectivaRobotica)
```

Para sincronizar los repositorios (web y local) se utilizan los siguientes comandos de git

```
git status
git add --all
git commit -m "algun_comentario"
git push -u origin main
```
Algunas veces que se empujen (<em>push</em>) los archivos del repositorio local al repositorio web desde el terminal por defecto de Raspbian hay que autenticar (usuario y contraseña) el perfil, sin embargo, se debe colocar una <em>Key</em>, siguiendo los siguientes pasos:<br>

https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

I. <br>
II. <br>
III. <br>

Si se tienen dos repositorios locales (dos computadores), es necesario actualizar el repositorio desactualizado, a través del siguiente comando:

```
git pull origin main
```

<h2>Introducción a Python :atom:</h2>

`Python` es un lenguaje de programación interpretado, entre sus principales ventajas están: facilidad de sintaxis, no necesita declarar variables, indispensable indentar las líneas de código, fácil manejo de arreglos (vectores y matrices)

<h3>1. Instalar `Python`</h3><br>
En Windows, descargar el instalador del siguiente link: https://www.python.org y al momento de instalarlo, seleccionar la opción Add path.<br>
En Raspbian, por defecto ya está instalado `Python` versión 3.1X

Para conocer la versión de `Python` sobre la cual se está trabajando, en el terminal ejecutar el siguiente comando: 

```
python --version
```

<h3>2. Instalar Visual Studio Code</h3><br>
En Windows, descargar el instalador del siguiente link: https://code.visualstudio.com<br>
En Raspbian, ejecutar en el terminal la siguiente línea de comando: 
```
sudo apt install code
```

<h3>3. Ejemplos de programación en Python</h3>

Para imprimir informacion se utiliza la funcion `print`, en la cual es posible inicializar un <em>string</em> en comillas simples o dobles.

```python
print("Hola mundo '2024'")
print('Hola mundo "2024"')
```

No hay necesidad de declarar variables, sin embargo, pueden ser inicializadas y específicamente a las variables numéricas se les puede modificar el tipo de variable.

print("vectors nums1: %s %d" %(nums1[1:4],nums1.size)) 
print("vectors nums1:",nums1[1:4],nums1.size) 
print("vectors nums1:"+str(nums1[1:4])+str(nums1.size))

```python
#Variables int y float
a = 7
b = c = 5.2
print(a,b,c)
print(type(a),type(int(b)),type(c)) #up o down casting
text = 'Los valores de a, b y c, respectivamente son:'
print(text+str(a)+' '+str(b)+" "+str(c)+"\n")

#Operaciones aritméticas
temp = a
a += b
print('a += b es: %f'%a)
a = temp
a -= b
print('a -= b es: %f'%a)
a = temp
a *= b
print('a *= b es: %f'%a)
a = temp
a /= b
print('a /= b es: %f'%a)
a = temp
d = a/2 #cociente float
e = a//2 #cociente int
f = a%2 #residuo float
print('Los valores de d, e y f, respectivamente son: %f, %f y %f'%(d,e,f))

```

Ademas, es posible realizar operaciones logicas con las variables numericas

``` python
num1 = 7
num2 = 2
equal = num1 == num2
different = num1 != num2
greater = num1 >= num2
less = num1 <= num2
print(equal, different, greater, less)
```

En el caso de variables tipo <em>string</em>, tambien se pueden hacer comparaciones, teniendo en cuenta los valores de codificacion Unicode (similar a ASCII)

``` python
word1 = "Hola"
word2 = "hola"
equal = word1 == word2
different = word1 != word2
greater = word1 >= word2
less = word1 <= word2
print(equal, different, greater, less)
```

Es posible acceder a un caracter determinado de un <em>string</em> a traves de una posición específica tanto de izquierda a derecha (incrementando) como de derecha a izquierda (decrementando).

```python
n = "Fabián"
i1 = n[4]
i2 = n[-2]
print(i1,i2)

```
Asi mismo, en `Python` se pueden obtener y concatenar diferentes caracteres de un <em>string</em> 

```python
n = "Fabián"
s = "Barrera Prieto"
o = 'PROFESOR'
a = '2024'

print("Primer apellido: %s" %s[:7])
print("Segundo apellido: %s" %s[8:])

c = n.upper()+' '+s+" es "+o.lower()+' en el semestre '+a+"\"2\""
print(c)
print(c[:int(len(c)/2)])
```
Para ingresar datos por teclado se utiliza la funcion `input`

```python
name = input('Ingrese el nombre \n') 
age = input("Ingrese la edad \n")
print('%s tiene %s años' %(name,age))
```
Arreglos

```python
import numpy

nums1 = numpy.array([3,7,4,9,1])
nums2 = numpy.array([[6.3,7.2,1.1],[9.6,5.7,2.4]])
print("Datos y tamaño del vector nums1: %s y %d" %(nums1[0:4],nums1.size))
print("Datos y tamaño del vector nums2: %s y %d(%d)" %(nums2,len(nums2),nums2.size)) 

nums1[2] = 100
nums2[0,:] = 83
print("Datos y tamaño del vector nums1: %s y %d" %(nums1[1:4],nums1.size))
print("Datos y tamaño del vector nums2: %s y %d(%d)" %(nums2,len(nums2),nums2.size)) 
```
Condicionales

```python
name = input('Ingrese el nombre \n') 
age = int(input("Ingrese la edad \n"))
if age>=0 and age<3:
    print('%s es un bebé' %(name))
elif age>=3 and age<12:
    print(name+" es un niño")
elif age>=12 and age<20:
    print(name, 'es un adolescente')
elif age>=20 and age<30:
    print('%s es un joven' %(name))
elif age>=30 and age<70:
    print('%s es un adulto' %(name))
elif age>=70:
    print('%s es un abuelo' %(name))
else:
    print("La edad no es válida")
```
Bucles o ciclos

```python
r = "S"
while r != 'n':
    name = input('Ingrese el nombre \n') 
    age = int(input("Ingrese la edad \n"))
    while age<=0:
        print('La edad no es válida')    
        age = int(input("Ingrese nuevamente la edad \n"))
    if age>=18:
        print("%s es mayor de edad \n" %name)   
    else:
        print("%s es menor de edad \n" %name)   
    
    r = input('Desea ingresar la información de otro estudiante (s/n) \n')
    
print('Fin') 
```

En algunas ocasiones resulta necesario utilizar un ciclo `while` para garantizar ciertas tareas durante un tiempo específico, teniendo en cuenta el temporizador de la librería `time`.

```python
import time

t1 = time.time()
t2 = 0.0
while t2 <= 20.0:
    print("El tiempo es %f s \n" %t2)
    t2 = time.time() - t1
```

Una suma es posible independizarla en una función, para que esta sea recursiva, flexible

```python
def sum(a,b):
    c = a + b
    return c

num1 = float(input('Ingrese el primer número: '))
num2 = float(input('Ingrese el segundo número: '))
num3 = sum(num1,num2)
print('%.2f + %.2f = %.2f' %(num1,num2,num3))
```

Arreglos y funciones

Este ejemplo es la serie de Fibonacci, la cual consiste en una sucesión que se calcula a partir de la suma de los dos últimos números de dicha sucesión

```python
def fibonacci(x):
    global data
    a = 1
    b = 1
    index = 0
    while index < x:
        data.append(a)
        temp = b
        b = a + b
        a = temp
        index += 1

data = []
fibonacci(12)
print(data)
```
Otro ejemplo son el ingreso de cinco calificaciones de un estudiantes y el cálculo del promedio de dichas notas, siendo que cada tarea se realiza en una función diferente

```python
def data():
    global grades
    for i in range(0,5,1):
        n = float(input('Ingrese la nota '+str(i+1)+" : "))
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
```

Clases



<h2>Toolbox Peter Corke</h2>

(https://petercorke.github.io/robotics-toolbox-python/intro.html)

1. Instalar el toolbox de Peter Corke en `Python` (https://github.com/petercorke/robotics-toolbox-python)

En Windows y en Raspbian, en el terminal ejecutar el siguiente comando:

```
pip3 install roboticstoolbox-python
```
>[!WARNING]
>En las últimas versiones de Raspbian se presenta el siguiente error posteriormente a la ejecución del comando anterior

![Alt text](image-2.png)

Para solucionar ese error, se deben tener en cuenta los siguientes pasos:

I. En el terminal, con los comandos linux (`cd`, `cd ..`, `ls`, `pwd`, etc.) entrar a la carpeta /etc<br>
II. Para abrir el archivo `pi.conf` en el terminal, ejecutar la siguiente línea de comando: 
```
sudo nano pip.conf
```
III. Al final del archivo agregar la siguiente línea: 
```
break-system-packages = true
```
IV. Presionar `Ctrl+x`, luego presionar la `s` para guardar las modificaciones y finalmente presionar `enter`

2. Ejecutar un código en `Python` donde se importe la libreria `roboticstoolbox` para verificar la correcta instalación de la misma

```python
from roboticstoolbox import *
import math

l1 = 12
l2 = 14
l3 = 6
l4 = 4

q1 = 0
q2 = 0

R = []
R.append(RevoluteDH(d=l1, alpha=math.pi/2, a=l2, offset=0))
R.append(RevoluteDH(d=l3, alpha=0, a=l4, offset=0))

Robot = DHRobot(R, name='Bender')
print(Robot)

Robot.teach([q1, q2], limits=[-30,30,-30,30,-30,30])

#zlim([-15,30]);

MTH = Robot.fkine([q1,q2])
print(MTH)
```

<h2>Interfaces gráficas (GUI) con Qt designer</h2>

1. Instalar Qt designer<br>
En Windows, descargar el software a través del siguiente link: https://build-system.fman.io/qt-designer-download<br>
En Raspbian, en el terminal ejecutar el siguiente comando: 
```
sudo apt-get install qtcreator
```

2. Realizar el <em>front</em> end de la interfaz gráfica para la suma aritmética de dos números editando algunas propiedades de cada <em>widget</em> utilizado.

![Alt text](image.png)

3. Convertir un archivo `.ui` a `.py`<br>

I. En el terminal, con los comandos linux (`cd`, `cd ..`, `ls`, `pwd`, etc.) entrar a la carpeta donde se encuentre el archivo `.ui`<br>

II. En Windows, ejecutar en el terminal el siguiente comando:
```
pyuic5 -x [FILENAME].ui -o [FILENAME].py (ej: pyuic5 -x suma.ui -o suma.py)
```
En Raspbian, ejecutar en el terminal el siguiente comando:
```
python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py (ej: python -m PyQt5.uic.pyuic -x suma.ui -o suma.py)
```

4. Realizar el <em>back end</em> de la interfaz gráfica, es decir, editar el archivo `.py` para que realice la tarea específica de la suma de dos números cuando se presione el botón.

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suma.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 270, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 150, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 160, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 170, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 170, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 160, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(200, 40, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 370, 201, 141))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(440, 370, 301, 151))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Aula2/ecci.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Acción al presionar el botón en la GUI
        self.pushButton.clicked.connect(self.Suma)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ejemplo1"))
        self.pushButton.setText(_translate("MainWindow", "CALCULAR"))
        self.label_2.setText(_translate("MainWindow", "+"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "="))
        self.label_4.setText(_translate("MainWindow", "SUMA ARITMÉTICA"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Prof. Fabián Barrera Prieto (MSc.)</p><p align=\"center\">Ingeniería mecatrónica</p><p align=\"center\">Electiva de robótica</p><p align=\"center\">2024-1</p></body></html>"))

    #Función que se ejecuta con la acción anterior
    def Suma(self):
        a = self.textEdit.toPlainText()
        b = self.textEdit_2.toPlainText()
        c = int(a)+int(b)
        self.label.setText(str(c))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
```
5. Ejecutar el archivo `.py` para probar la aplicación

![Alt text](image-1.png)