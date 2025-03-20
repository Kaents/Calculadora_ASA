from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QStackedWidget
import sys
import calculate_ark

class CalculateArkGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora ASA")
        self.setGeometry(100, 100, 400, 300)

        # Crear el QstackedWidget para manejar las diferentes vistas
        self.stack = QStackedWidget()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.stack)

        # Creacion de las vistas
        self.pag_main = self.create_main_page()
        self.pag_reaper = self.create_reaper_page()
        self.pag_tek = self.create_tek_page()

        # Agreamos las vistas al stack
        self.stack.addWidget(self.pag_main)
        self.stack.addWidget(self.pag_reaper)
        self.stack.addWidget(self.pag_tek)

        # Mostramos la página principal al inicio
        self.stack.setCurrentWidget(self.pag_main)

    def create_main_page(self):
        """Creamos la página principal con los botones para seleccionar el resto"""
        pagine = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Seleccione una opción:")
        layout.addWidget(label)

        btn_reaper = QPushButton("Calcular nivel de Reaper")
        btn_reaper.clicked.connect(lambda: self.stack.setCurrentWidget(self.pag_reaper))
        layout.addWidget(btn_reaper)

        btn_tek = QPushButton("Conversión de Tek")
        btn_tek.clicked.connect(lambda: self.stack.setCurrentWidget(self.pag_tek))
        layout.addWidget(btn_tek)

        pagine.setLayout(layout)
        return pagine

    def create_reaper_page(self):
        """Creamos la página para calcular el nivel de la Reaper que nacera"""
        pagine = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Calcular nivel de Reaper")
        layout.addWidget(label)

        self.input_r = QLineEdit()
        self.input_r.setPlaceholderText("Nivel de la Reaper")
        layout.addWidget(self.input_r)

        self.input_p = QLineEdit()
        self.input_p.setPlaceholderText("Nivel de tu personaje")
        layout.addWidget(self.input_p)

        btn_calculate = QPushButton("Calcular")
        btn_calculate.clicked.connect(self.calculate_reaper_level)
        layout.addWidget(btn_calculate)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        # Botón para volver a la página principal
        btn_back = QPushButton("Volver")
        btn_back.clicked.connect(lambda: self.stack.setCurrentWidget(self.pag_main))
        layout.addWidget(btn_back)

        pagine.setLayout(layout)
        return pagine
    
    def calculate_reaper_level(self):
        """Calculamos el nivel de la Reaper"""
        try:
            r = int(self.input_r.text())
            p = int(self.input_p.text())
            final_level = calculate_ark.calculate_level(r, p)
            self.result_label.setText(f"Nivel de la Reaper por nacer: {final_level}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese valores válidos.")
    
    def create_tek_page(self):
        """Creamos la página para convertir tek"""
        pagine = QWidget()
        layout = QVBoxLayout()

        label = QLabel("Conversión de Tek")
        layout.addWidget(label)

        self.input_tek = QLineEdit()
        self.input_tek.setPlaceholderText("Cantidad de Tek")
        layout.addWidget(self.input_tek)

        btn_convert = QPushButton("Convertir")
        btn_convert.clicked.connect(self.convert_tek)
        layout.addWidget(btn_convert)

        self.result_label_tek = QLabel("")
        layout.addWidget(self.result_label_tek)

        # Botón para volver a la página principal
        btn_back = QPushButton("Volver")
        btn_back.clicked.connect(lambda: self.stack.setCurrentWidget(self.pag_main))
        layout.addWidget(btn_back)

        pagine.setLayout(layout)
        return pagine
    
    def convert_tek(self):
        """Convertimos la cantidad de tek"""
        try:
            quantity_tek = int(self.input_tek.text())
            result = calculate_ark.convertion_tek(quantity_tek)
            result_text = "\n".join([f"{item}: {value}" for item, value in result.items()])
            self.result_label_tek.setText(f"Conversion de Tek:\n{result_text}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese una cantidad válida.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculateArkGUI()
    window.show()
    sys.exit(app.exec())