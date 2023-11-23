import math
import sys
from par import *
from hola import *
from ess import *
from wes import *
from PyQt5 import QtWidgets, uic
from tkinter import messagebox

import sqlite3 as sql
import sys
import sqlite3 as sql
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QLineEdit

from sympy import symbols, expand, factor, solve, simplify, roots, solveset, Rational

app = QtWidgets.QApplication([])

login = uic.loadUi("Mate.ui")
nuevo = uic.loadUi("Login1_0.ui")
ven = uic.loadUi("Aplicacion.ui")
bloque1 = uic.loadUi("Bloque_1.ui")
bloque2 = uic.loadUi("Bloque_2.ui")
bloque3 = uic.loadUi("Bloque_3.ui")

try:
    con = sql.connect("Base1.db")
    con.commit()
    con.close()
except:
    print("Error en la base de datos")

def gui_login():
    name = login.lineEdit_3.text()
    password = login.lineEdit_4.text()
    if len(name) == 0 or len(password) == 0:
        messagebox.showwarning("EROR", "Provide all the details or register.")
    else:
        con = sql.connect("Base1.db")
        cursor = con.cursor()
        cursor.execute('SELECT nombre, contraseña FROM usuarios WHERE nombre = ? AND contraseña = ?', (name, password))
    if cursor.fetchall():
        gui_ven()
    else:
        messagebox.showwarning("ERROR", "Incorrect Username or Password")


def tabla():
    con = sql.connect("Base1.db")
    cursor = con.cursor()
    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS usuarios (
            nombre text,
            contraseña text
        )"""

    )
    con.commit()
    con.close()

def registrar(nombre, contraseña):
    con = sql.connect("Base1.db")
    cursor = con.cursor()
    instruccion = f"INSERT INTO usuarios VALUES ('{nombre}',"\
                  f"'{contraseña}')"
    cursor.execute(instruccion)
    con.commit()
    con.close()

def datos():
    nombre = nuevo.lineEdit.text()
    contraseña = nuevo.lineEdit_2.text()
    contraseña_2 = nuevo.lineEdit_3.text()
    if contraseña != contraseña_2:
        messagebox.showinfo("ERROR", "THE PASSWORDS AREN'T THE SAME")
    elif contraseña == contraseña_2:
        registrar(nombre, contraseña)
        messagebox.showinfo("Succesfully", "You're Registered")
        nuevo.lineEdit.setText("")
        nuevo.lineEdit_2.setText("")
        nuevo.lineEdit_3.setText("")

def diferencia():
    a = float(bloque1.lineEdit.text())
    b = float(bloque1.lineEdit_2.text())

    # Obtener los textos desde los line edits en bloque2
    e_text = bloque1.lineEdit_8.text()
    x_text = bloque1.lineEdit_9.text()

    # Convertir los textos a símbolos solo si los campos no están vacíos
    e = symbols(e_text) if e_text else 1  # Si e_text está vacío, d se establece en 1
    d = symbols(x_text) if x_text else 1  # Si x_text está vacío, e se establece en 1

    if any(root % 1 != 0 for root in [math.sqrt(a), math.sqrt(b)]):
        bloque1.lineEdit_3.setText("Error: No se puede resolver")
    else:
     resultado_formateado = f"({math.sqrt(b)*e} + {math.sqrt(a)*d})*({math.sqrt(b)*e} - {math.sqrt(a)*d})"
     bloque1.lineEdit_3.setText(str(resultado_formateado))


def trinomio_cuadrado():
    a = int(bloque1.lineEdit_4.text())
    b = int(bloque1.lineEdit_5.text())
    c = int(bloque1.lineEdit_7.text())

    # Verificar si sqrt(a) y sqrt(c) tienen decimales (excepto .0)
    if any(root % 1 != 0 for root in [math.sqrt(a), math.sqrt(c)]):
        bloque1.lineEdit_6.setText("Error: No se puede resolver")
    else:
        # Calcular la variable f multiplicando las raíces de a y c por 2
        f = 2 * math.sqrt(a) * math.sqrt(c)

        # Verificar si la variable f es igual a b
        if f == b:
            # Definir el símbolo x
            x = symbols('x')

            # Formatear la expresión como (ax + b)^2
            resultado_formateado = f"({math.sqrt(a)}*x + {math.sqrt(c)})^2"

            # Mostrar el resultado en el QLineEdit
            bloque1.lineEdit_6.setText(resultado_formateado)
        else:
            bloque1.lineEdit_6.setText("Error: No se puede resolver")
def cuadrado():
    c = float(bloque2.lineEdit_2.text())
    d = float(bloque2.lineEdit_3.text())

    # Obtener los textos de los QLineEdit
    e_text = bloque2.lineEdit.text()
    x_text = bloque2.lineEdit_8.text()

    # Convertir los textos a símbolos solo si los campos no están vacíos
    a = symbols(e_text) if e_text else 1  # Si e_text está vacío, a se establece en 1
    b = symbols(x_text) if x_text else 1  # Si x_text está vacío, b se establece en 1

    # Realizar la operación
    f = (((c * a)) + (d * b)) ** 2
    f_expand = expand(f)

    # Establecer el resultado en un QLineEdit
    bloque2.lineEdit_7.setText(str(f_expand))

def cubo():
    c = float(bloque2.lineEdit_4.text())
    d = float(bloque2.lineEdit_5.text())

    # Obtener los textos de los QLineEdit
    e_text = bloque2.lineEdit_9.text()
    x_text = bloque2.lineEdit_10.text()

    # Convertir los textos a símbolos solo si los campos no están vacíos
    a = symbols(e_text) if e_text else 1  # Si e_text está vacío, a se establece en 1
    b = symbols(x_text) if x_text else 1  # Si x_text está vacío, b se establece en 1

    # Realizar la operación
    f = ((c * a) + (d * b)) ** 3
    f_expand = expand(f)

    # Establecer el resultado en un QLineEdit
    bloque2.lineEdit_6.setText(str(f_expand))

def segundo():
    a = float(bloque3.lineEdit_4.text())
    b = float(bloque3.lineEdit_5.text())
    c = float(bloque3.lineEdit_8.text())

    d = (b * b) - 4 * a * c

    if d < 0:
        messagebox.showinfo("ERROR", "No existen soluciones")
    else:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)

        bloque3.lineEdit_6.setText(str(x1))
        bloque3.lineEdit_12.setText(str(x2))

def trinomio2():
    d = float(bloque3.lineEdit_9.text())
    b = float(bloque3.lineEdit_10.text())
    c = float(bloque3.lineEdit_11.text())
    x = symbols('x')
    a = math.sqrt(d)

    f = a*x**2 + b*x + c

    solucion = solve(f)

    solucion1, solucion2 = solucion
    if any(sol % 1 != 0 for sol in solucion):
        bloque3.lineEdit_7.setText("Error: No soluciones enteras")
    else:
        solucion1, solucion2 = [int(sol) for sol in solucion]  # Convertir a enteros
        bloque3.lineEdit_7.setText(str((a*x - solucion1)*(a*x - solucion2)))

def binomio():
    messagebox.showinfo("Información", "Un binomio al cuadrado se refiere a la expresión matemática (a + b)^2, donde 'a' y 'b'"
                                       " pueden representar números o variables. Al expandir esta expresión, obtenemos a^2 + 2ab + b^2. Esta fórmula es fundamental en álgebra "
                                       "y se utiliza para simplificar expresiones cuadráticas y resolver problemas algebraicos avanzados.")
def binomio2():
    messagebox.showinfo("Información", "Un binomio al cubo se refiere a la expresión matemática (a + b)^3, donde 'a' y 'b' pueden representar números o variables. Al expandir esta expresión, obtenemos a^3 + 3a^2b + 3ab^2 + b^3. Esta fórmula es crucial en álgebra y se utiliza para resolver problemas más complejos y desarrollar habilidades matemáticas avanzadas.")
def trinomio1():
    messagebox.showinfo("Información","Un trinomio de la forma x^2 + bx + c, es una expresión algebraica cuadrática. En esta fórmula, 'b' y 'c' son coeficientes que representan números reales o variables. La resolución de este trinomio implica la factorización, la fórmula cuadrática o completar el cuadrado, y es esencial en el álgebra para resolver ecuaciones y problemas aplicados.")
def ecuacion():
    messagebox.showinfo("Información","La ecuación general de segundo grado es de la forma ax^2 + bx + c = 0, donde 'a', 'b' y 'c' son coeficientes, pudiendo ser números reales o variables. Se resuelve utilizando la fórmula cuadrática, que es (-b ± √(b^2 - 4ac)) / 2a. Esta ecuación es fundamental para resolver problemas cuadráticos en álgebra.")
def Trinomio():
    messagebox.showinfo("Información"," Un trinomio cuadrado perfecto es una expresión algebraica con tres términos que puede ser factorizada como el cuadrado de un binomio. Por ejemplo,  a^2 + 2ab + b^2 es un trinomio cuadrado perfecto donde el binomio es a+b. La factorización revela la forma  (a+b)^2  , simplificando cálculos algebraicos. Este tipo de trinomios es fundamental en álgebra y ecuaciones cuadráticas.")
def diferencia1():
    messagebox.showinfo("Información","La diferencia de cuadrados es un patrón algebraico representado por la expresión  a^2 - b ^2 . Puede factorizarse como  (a+b)(a−b), donde  a y  b son números o expresiones algebraicas. Esta factorización es esencial en simplificar y resolver ecuaciones y polinomios.")
def gui_ven():
    login.hide()
    ven.show()

def block1():
    ven.hide()
    bloque1.show()

def block2():
    ven.hide()
    bloque2.show()

def block3():
    ven.hide()
    bloque3.show()
def gui_nuevo():
    login.hide()
    nuevo.show()
    tabla()


def gui_regresar1():

    nuevo.hide()
    login.show()


def gui_regresar2():

    login.lineEdit_3.setText("")
    login.lineEdit_4.setText("")
    ven.hide()
    login.show()
def borrar1():
    bloque1.lineEdit.setText("")
    bloque1.lineEdit_2.setText("")
    bloque1.lineEdit_3.setText("")
    bloque1.lineEdit_4.setText("")
    bloque1.lineEdit_5.setText("")
    bloque1.lineEdit_6.setText("")
    bloque1.lineEdit_7.setText("")
    bloque1.lineEdit_8.setText("")
    bloque1.lineEdit_9.setText("")

def borrar2():
        bloque2.lineEdit.setText("")
        bloque2.lineEdit_2.setText("")
        bloque2.lineEdit_3.setText("")
        bloque2.lineEdit_4.setText("")
        bloque2.lineEdit_5.setText("")
        bloque2.lineEdit_6.setText("")
        bloque2.lineEdit_7.setText("")
        bloque2.lineEdit_8.setText("")
        bloque2.lineEdit_9.setText("")
        bloque2.lineEdit_10.setText("")


def borrar3():
    bloque3.lineEdit_9.setText("")
    bloque3.lineEdit_10.setText("")
    bloque3.lineEdit_11.setText("")
    bloque3.lineEdit_7.setText("")
    bloque3.lineEdit_4.setText("")
    bloque3.lineEdit_5.setText("")
    bloque3.lineEdit_8.setText("")
    bloque3.lineEdit_6.setText("")
    bloque3.lineEdit_12.setText("")


def gui_regresar3():
    bloque1.hide()
    bloque2.hide()
    bloque3.hide()
    ven.show()
def salir():
    app.exit()
# botones

login.pushButton_3.clicked.connect(gui_login)
login.pushButton.clicked.connect(gui_nuevo)
nuevo.pushButton_2.clicked.connect(gui_regresar1)
ven.pushButton_4.clicked.connect(gui_regresar2)
ven.pushButton.clicked.connect(block1)
ven.pushButton_2.clicked.connect(block2)
ven.pushButton_3.clicked.connect(block3)
nuevo.pushButton.clicked.connect(datos)
login.pushButton_2.clicked.connect(salir)


bloque1.pushButton_3.clicked.connect(gui_regresar3)
bloque1.pushButton_4.clicked.connect(salir)
bloque1.pushButton_2.clicked.connect(trinomio_cuadrado)
bloque1.pushButton.clicked.connect(diferencia)
bloque1.pushButton_5.clicked.connect(diferencia1)
bloque1.pushButton_6.clicked.connect(Trinomio)
bloque1.pushButton_7.clicked.connect(borrar1)

bloque2.pushButton_3.clicked.connect(gui_regresar3)
bloque2.pushButton_4.clicked.connect(salir)
bloque2.pushButton.clicked.connect(cuadrado)
bloque2.pushButton_2.clicked.connect(cubo)
bloque2.pushButton_5.clicked.connect(binomio)
bloque2.pushButton_6.clicked.connect(binomio2)
bloque2.pushButton_7.clicked.connect(borrar2)

bloque3.pushButton_3.clicked.connect(gui_regresar3)
bloque3.pushButton_4.clicked.connect(salir)
bloque3.pushButton_2.clicked.connect(segundo)
bloque3.pushButton.clicked.connect(trinomio2)
bloque3.pushButton_5.clicked.connect(trinomio1)
bloque3.pushButton_6.clicked.connect(ecuacion)
bloque3.pushButton_7.clicked.connect(borrar3)

login.show()

app.exec()



def msg_about(title, message):
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Information)
    msgBox.setWindowTitle(title)
    msgBox.setText(message)
    msgBox.setStandardButtons(QMessageBox.Ok)
    returnValue = msgBox.exec()
    if returnValue == QMessageBox.Ok:
        pass

