import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QStackedWidget, QListWidget, QListWidgetItem)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

#Fuinción de la lista de la equivalencia de 100 tek.
def convertion_tek(quantity_tek):
    convertion = {
        'Tek Celling': 100,
        'Tek Wall': 120,
        'Tek Pillar': 200,
        'Tek Large Walls': 30,
        'Tek Roof/Ramp/Stairs': 100,
        'Tek Sloped Walls': 350,
        'Tek Foundation': 80,
        'Tek Triangle Fundation': 200,
        'Tek Vaccum Compartments': 20,
        'Tek Generator': 3,
        'Tek Replicator': 1,
        'Tek Cloning Chamber': 1,
        'Tek Dedicated Storage': 30,
        'Tek Transmiter': 3,
        'Tek Trough': 5,
        'Tek Triangle Ceiling': 200,
        'Medium TP': 4,
        'Hard Poly': 10000,
        'Black Perls': 1000,
        'Metal Lingots': 20000,
        'Crystal': 40000
    }
    return {item: round((quantity_tek / 100) * value) for item, value in convertion.items()}

#Calculo de niveles de embriones en el juego Reapers
def calculate_level(r, p):
    e = r * (p + 100) / 250
    final_level = int(e + 75)
    return final_level

#Clase de la ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora de Embviones Reapears y Conversion Tek')
        self.setFixedSize(400, 400)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.menu_start()
        self.menu_calculate()
        self.menu_convertion()

        self.stack.setCurrentIndex(0)

#Ventana aplicada a al calculo de niveles de embriones.
    def menu_start(self):
        widget = QWidget()
        layout = QVBoxLayout()

        laber = QLabel('Seleccione una opción:')
        layout.addWidget(laber)

        btn_calculate = QPushButton('Calcular nivel de embrion')
        btn_calculate.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        layout.addWidget(btn_calculate)

        btn_convertion = QPushButton('Conversion Tek')
        btn_convertion.clicked.connect(lambda: self.stack.setCurrentIndex(2))
        layout.addWidget(btn_convertion)

        widget.setLayout(layout)
        self.stack.addWidget(widget)

#Calculo de nivel.
    def menu_calculate(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.input_r = QLineEdit()
        self.input_r.setPlaceholderText('Nivel de la Reaper.')
        layout.addWidget(self.input_r)

        self.input_p = QLineEdit()
        self.input_p.setPlaceholderText('Nivel de tu Personaje.')
        layout.addWidget(self.input_p)

        self.btn_calculate = QPushButton('Calcular')
        self.btn_calculate.clicked.connect(self.view_level)
        layout.addWidget(self.btn_calculate)

        self.label_final_level = QLabel()
        layout.addWidget(self.label_final_level)

        btn_back = QPushButton('Volver al manú.')
        btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        layout.addWidget(btn_back)

        widget.setLayout(layout)
        self.stack.addWidget(widget)

#Vista resultado del calculo de niveles de embriones.
    def view_level(self):
        try:
            r = int(self.input_r.text())
            p = int(self.input_p.text())
            final_level = calculate_level(r, p)
            self.label_final_level.setText(f'El nivel del embrion es: {final_level}')
        except ValueError:
            self.label_final_level.setText('Error de parametros: Ingrese solo número enteros')

#Ventana aplicada a la conversion tek.
    def menu_convertion(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.input_tek = QLineEdit()
        self.input_tek.setPlaceholderText('Ingresa la cantidad de Tek.')
        layout.addWidget(self.input_tek)

        self.btn_convertion2 = QPushButton('Convertir')
        self.btn_convertion2.clicked.connect(self.view_convertion)
        layout.addWidget(self.btn_convertion2)

        self.list_convertion = QListWidget()
        layout.addWidget(self.list_convertion)

        btn_back = QPushButton('Volver al menú.')
        btn_back.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        layout.addWidget(btn_back)

        widget.setLayout(layout)
        self.stack.addWidget(widget)
    
#Resultado de la conversion tek de la lista.
    def view_convertion(self):
        try:
            quantity_tek = int(self.input_tek.text())
            convertion = convertion_tek(quantity_tek)
            self.list_convertion.clear()
            for item, value in convertion.items():
                item = QListWidgetItem(f'{item}: {value}')
                self.list_convertion.addItem(item)
        
        except ValueError:
            item = QListWidgetItem('Error de parametros: Ingrese un número valido')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())