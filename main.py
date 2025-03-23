from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QStackedWidget,  QHBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sys
import calculate_ark


def set_background(widget, image_path):
        """Establece la imagen de fondo para la ventana principal."""
        label_background = QLabel(widget)
        pixmap = QPixmap(image_path)
        label_background.setPixmap(pixmap)
        label_background.setScaledContents(True)
        label_background.resize(widget.size())
        label_background.lower()


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


    @staticmethod
    def load_styles(app):
        try:
            with open("styles/style.qss", "r") as file:
                app.setStyleSheet(file.read())
        except FileNotFoundError:
            print("El archivo de estilos no se encontró. Usando estilos predeterminados.")

    
    def create_main_page(self):
        """Creamos la página principal con los botones para seleccionar el resto"""
        pagine = QWidget()
        pagine.setObjectName("page_main")

        layout = QVBoxLayout()

        label_tittle = QLabel("Seleccione una opción:")
        label_tittle.setObjectName("tittle")
        label_tittle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_tittle)

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
        pagine.setObjectName("page_reaper")

        layout = QVBoxLayout()

        label_tittle2 = QLabel("Calcular nivel de Reaper")
        label_tittle2.setObjectName("tittle")
        label_tittle2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label_tittle2)

        label_reaper = QLabel("Nivel de la Reaper")
        label_reaper.setObjectName("label_input")
        layout.addWidget(label_reaper)

        self.input_r = QLineEdit()
        layout.addWidget(self.input_r)

        label_carachter = QLabel("Nivel de tu personaje")
        label_carachter.setObjectName("label_input")
        layout.addWidget(label_carachter)

        self.input_p = QLineEdit()
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
        pagine.setObjectName("page_convertion")

        layout = QVBoxLayout()

        label = QLabel("Conversión de Tek")
        label.setObjectName("tittle")
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
    CalculateArkGUI.load_styles(app)
    window = CalculateArkGUI()
    window.show()
    sys.exit(app.exec())