from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from gui.mainMenu_ui import Ui_MainWindow
from gui.simulation import Ui_MainWindow as Ui_SimulationWindow
import sys
import os

from utils.operation_generator import OperationGenerator
from gui.save_dialog import ask_save_generated
from utils.op_parser import OperationParser

class SimulationWindow(QMainWindow):
    def __init__(self, parent=None):
        # accept an optional parent so callers can pass a parent window
        super().__init__(parent)
        self.ui = Ui_SimulationWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Simulador de Paginación - Simulación")

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.simulation_window = SimulationWindow(self)
        self.ui.setupUi(self)
        self.setWindowTitle("Simulador de Paginación - Menú Principal")

        self.ui.exitBtn.clicked.connect(self.close)
        self.ui.startBtn.clicked.connect(self.start_simulation)
        self.ui.browseBtn.clicked.connect(self.select_file)

        self.ui.algCombo.addItems(["FIFO", "Second Chance", "MRU", "Random"])
        self.ui.processCombo.addItems(["10", "50", "100"])
        self.ui.operationCombo.addItems(["500", "1000", "5000"])
        

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar archivo de operaciones",
            "",
            "Archivos de simulación (*.page);;Todos los archivos (*.*)"
        )
        if file_name:
            self.ui.fileEdit.setText(file_name)


    def start_simulation(self):
        try:
            seed = self.ui.seedSpin.value()
            algorithm = self.ui.algCombo.currentText()
            num_processes = int(self.ui.processCombo.currentText())
            num_operations = int(self.ui.operationCombo.currentText())
            file_path = self.ui.fileEdit.text().strip()
            
            if file_path:
                if not os.path.exists(file_path):
                    QMessageBox.warning(self, "Error", "El archivo seleccionado no existe")
                    return
                # Cargar y parsear operaciones desde archivo
                try:
                    parser = OperationParser()
                    operations = parser.parse_file(file_path)

                    # Imprimir operaciones cargadas en consola
                    # print(f"Cargadas {len(operations)} operaciones desde: {file_path}")
                    # for i, op in enumerate(operations, 1):
                    #     print(f"{i}: {op}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"No se pudieron parsear las operaciones: {e}")
                    return
            else:
                gen = OperationGenerator()
                operations = gen.generate_operations(num_processes, num_operations, seed)
                if ask_save_generated(self):
                    save_path, _ = QFileDialog.getSaveFileName(
                        self,
                        "Guardar archivo de operaciones",
                        "",
                        "Archivos de simulación (*.page);;Todos los archivos (*.*)"
                    )
                    if save_path:
                        try:
                            gen.save_operations(operations, save_path)
                            QMessageBox.information(self, "Guardado", f"Archivo guardado en: {save_path}")
                        except Exception as e:
                            QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo: {e}")
            
            print(f"Semilla: {seed}, Algoritmo: {algorithm}, Procesos: {num_processes}, Operaciones: {num_operations}")
            self.simulation_window.show()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al iniciar simulación: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
