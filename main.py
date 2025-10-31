from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QHBoxLayout, QFrame
from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor, QBrush
from gui.mainMenu_ui import Ui_MainWindow
from gui.simulation import Ui_MainWindow as Ui_SimulationWindow
import sys
import os

from utils.operation_generator import OperationGenerator
from gui.save_dialog import ask_save_generated
from utils.op_parser import OperationParser
from core.simulation_engine import SimulationEngine

class SimulationWindow(QMainWindow):
    def __init__(self, engine, parent=None):
        super().__init__(parent)
        self.ui = Ui_SimulationWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Simulador de Paginación - Simulación")
        
        # Referencia al engine
        self.engine = engine
        
        # Estado
        self.is_paused = False
        self.pid_colors = {}
        
        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.step_simulation)
        self.timer_interval = 100  #ms entre steps
        
        self.ui.pushButton.clicked.connect(self.pause_resume)  # Pausar/Reanudar
        self.ui.pushButton_2.clicked.connect(self.reset_simulation)  # Reiniciar
        self.ui.pushButton_3.clicked.connect(self.go_back)  # Volver
        
        # Inicializar grillas de RAM (100 celdas por RAM)
        self.opt_ram_cells = self._init_ram_grid(self.ui.frame_2)
        self.sel_ram_cells = self._init_ram_grid(self.ui.frame_3)

        # Actualizar display inicial
        self.update_display()
        
        self.start_simulation()
    
    def update_display(self):
        stats = self.engine.get_statistics()
        
        # Actualizar stats de OPT (lado izquierdo)
        opt_stats = stats['opt']
        self.ui.label_6.setText(f"Processes: {stats['active_processes']}")
        self.ui.label_7.setText(f"Sim-Time: {opt_stats['clock']}s")
        self.ui.label_8.setText(f"RAM KB: {opt_stats['ram_used_kb']:.2f}")
        self.ui.label_9.setText(f"RAM %: {opt_stats['ram_percent']:.1f}%")
        self.ui.label_4.setText(f"V-RAM KB: {opt_stats['vram_used_kb']:.2f}")
        self.ui.label_5.setText(f"V-RAM %: {opt_stats['vram_percent']:.1f}%")
        self.ui.label_10.setText(f"LOADED: {opt_stats['loaded_pages']}")
        self.ui.label_11.setText(f"UNLOADED: {opt_stats['unloaded_pages']}")
        self.ui.label_14.setText(f"{opt_stats['thrashing_time']}s")
        self.ui.label_15.setText(f"{opt_stats['thrashing_percent']:.1f}%")
        self.ui.label_16.setText(f"Fragmentación: {opt_stats['fragmentation_kb']:.2f} KB")
        
        # Actualizar stats del algoritmo seleccionado (lado derecho)
        sel_stats = stats['selected']
        self.ui.label_56.setText(f"Processes: {stats['active_processes']}")
        self.ui.label_51.setText(f"Sim-Time: {sel_stats['clock']}s")
        self.ui.label_53.setText(f"RAM KB: {sel_stats['ram_used_kb']:.2f}")
        self.ui.label_54.setText(f"RAM %: {sel_stats['ram_percent']:.1f}%")
        self.ui.label_48.setText(f"V-RAM KB: {sel_stats['vram_used_kb']:.2f}")
        self.ui.label_46.setText(f"V-RAM %: {sel_stats['vram_percent']:.1f}%")
        self.ui.label_52.setText(f"LOADED: {sel_stats['loaded_pages']}")
        self.ui.label_49.setText(f"UNLOADED: {sel_stats['unloaded_pages']}")
        self.ui.label_50.setText(f"{sel_stats['thrashing_time']}s")
        self.ui.label_45.setText(f"{sel_stats['thrashing_percent']:.1f}%")
        self.ui.label_57.setText(f"Fragmentación: {sel_stats['fragmentation_kb']:.2f} KB")
        
        alg_name = self.engine.mmu_selected.algorithm.__class__.__name__
        self.ui.label_3.setText(f"RAM - {alg_name}")
        self.ui.label_44.setText(f"MMU - {alg_name}")
        
        # Actualizar tablas
        self.update_page_table(self.ui.tableWidget, stats['opt_pages'], current_clock=self.engine.mmu_opt.clock)
        self.update_page_table(self.ui.tableWidget_3, stats['selected_pages'], current_clock=self.engine.mmu_selected.clock)

        # Resaltar thrashing > 50%
        opt_thrashing_style = "color: red; font-weight: bold;" if opt_stats['thrashing_percent'] > 50 else ""
        sel_thrashing_style = "color: red; font-weight: bold;" if sel_stats['thrashing_percent'] > 50 else ""
        self.ui.label_15.setStyleSheet(opt_thrashing_style)
        self.ui.label_45.setStyleSheet(sel_thrashing_style)

        # Actualizar visualización de RAM
        self._update_ram_frames()
    
    def update_page_table(self, table, pages_info, current_clock):
        
        table.setRowCount(len(pages_info))
        
        # Llenar cada fila con datos
        for row, page in enumerate(pages_info):
            # Columna 0: PAGE ID
            table.setItem(row, 0, QTableWidgetItem(str(page['page_id'])))
            
            # Columna 1: PID
            table.setItem(row, 1, QTableWidgetItem(str(page['pid'])))
            
            # Columna 2: LOADED (X si esta en RAM, si no vacio)
            table.setItem(row, 2, QTableWidgetItem(page['loaded']))
            
            # Columna 3: L-ADDR (Logical Address = page_id)
            table.setItem(row, 3, QTableWidgetItem(str(page['logical_addr'])))
            
            # Columna 4: M-ADDR (Physical/Memory Address)
            m_addr = str(page['physical_addr']) if page['physical_addr'] is not None else ''
            table.setItem(row, 4, QTableWidgetItem(m_addr))
            
            # Columna 5: D-ADDR (Disk Address)
            d_addr = str(page['disk_addr']) if page['disk_addr'] is not None else ''
            table.setItem(row, 5, QTableWidgetItem(d_addr))
            
            # Columna 6: LOADED-T (tiempo cargado en RAM)
            if page['loaded'] == 'X' and page['loaded_time'] is not None:
                time_loaded = current_clock - page['loaded_time']
                if time_loaded >= 0:
                    table.setItem(row, 6, QTableWidgetItem(f"{time_loaded}s"))
                else:
                    table.setItem(row, 6, QTableWidgetItem(''))
            else:
                table.setItem(row, 6, QTableWidgetItem(''))
            
            # Columna 7: MARK (Reference bit)
            table.setItem(row, 7, QTableWidgetItem(page['mark']))

            # Colorear la fila según el PID
            pid = page['pid']
            color = self._get_color_for_pid(pid)
            self._apply_row_color(table, row, color)
    
    def start_simulation(self):
        self.is_paused = False
        self.ui.pushButton.setText("Pausar")
        self.timer.start(self.timer_interval)
    
    def step_simulation(self):
        if not self.is_paused and not self.engine.is_finished:

            success = self.engine.step()
            
            self.update_display()
            
            if self.engine.is_finished:
                self.timer.stop()
                self.ui.pushButton.setText("Finalizado")
                self.ui.pushButton.setEnabled(False)
    
    def pause_resume(self):
        if self.engine.is_finished:
            return
        
        self.is_paused = not self.is_paused
        
        if self.is_paused:
            self.ui.pushButton.setText("Reanudar")
        else:
            self.ui.pushButton.setText("Pausar")
    
    def reset_simulation(self):

        self.timer.stop()
        
        # Reiniciar engine
        alg_name = self.engine.mmu_selected.algorithm.__class__.__name__
        seed = getattr(self.engine.mmu_selected.algorithm, 'seed', None)
        self.engine = SimulationEngine(self.engine.operations, alg_name, seed)
        
        # Reiniciar estado
        self.is_paused = False
        self.ui.pushButton.setText("Pausar")
        self.ui.pushButton.setEnabled(True)
        
        self.update_display()
        
        self.timer.start(self.timer_interval)
        
    def go_back(self):
        self.timer.stop()
        self.close()

    def _init_ram_grid(self, frame: QFrame):

        layout = QHBoxLayout()
        layout.setContentsMargins(4, 4, 4, 4)
        layout.setSpacing(1)
        frame.setLayout(layout)

        cells = []
        for _ in range(100):
            cell = QFrame(frame)
            cell.setObjectName("ramCell")
            cell.setMinimumHeight(24)
            cell.setStyleSheet("background-color: #e0e0e0; border: 1px solid #bdbdbd;")
            layout.addWidget(cell, 1)
            cells.append(cell)
        return cells

    def _get_color_for_pid(self, pid: int) -> QColor:
        if pid not in self.pid_colors:
            hue = (pid * 137) % 360
            color = QColor()
            color.setHsv(hue, 180, 220)
            self.pid_colors[pid] = color
        return self.pid_colors[pid]

    def _apply_row_color(self, table, row: int, color: QColor):
        r, g, b, _ = color.getRgb()
        luminance = (0.299 * r + 0.587 * g + 0.114 * b)
        text_color = QColor(0, 0, 0) if luminance > 140 else QColor(255, 255, 255)
        brush_bg = QBrush(color)
        brush_fg = QBrush(text_color)
        col_count = table.columnCount()
        for col in range(col_count):
            item = table.item(row, col)
            if item is None:
                item = QTableWidgetItem("")
                table.setItem(row, col, item)
            item.setBackground(brush_bg)
            item.setForeground(brush_fg)

    def _update_ram_frames(self):
        # OPT
        opt_mem = getattr(self.engine.mmu_opt, 'physical_memory', [])
        opt_clock = getattr(self.engine.mmu_opt, 'clock', 0)
        for idx in range(min(100, len(self.opt_ram_cells))):
            cell = self.opt_ram_cells[idx]
            page = opt_mem[idx] if idx < len(opt_mem) else None
            if page is None:
                cell.setStyleSheet("background-color: #e0e0e0; border: 1px solid #bdbdbd;")
                cell.setToolTip(f"Frame {idx}: vacío")
            else:
                color = self._get_color_for_pid(getattr(page, 'pid', 0))
                hex_color = color.name()
                cell.setStyleSheet(f"background-color: {hex_color}; border: 1px solid #424242;")
                pid = getattr(page, 'pid', '?')
                page_id = getattr(page, 'page_id', '?')
                ptr = getattr(page, 'ptr', '?')
                loaded_time = getattr(page, 'loaded_time', None)
                t_loaded = (opt_clock - loaded_time) if (loaded_time is not None and opt_clock >= loaded_time) else None
                t_loaded_str = f"{t_loaded}s" if t_loaded is not None else "-"
                cell.setToolTip(f"Frame {idx}\nPID: {pid}\nPage: {page_id}\nPtr: {ptr}\nLoaded-T: {t_loaded_str}")

        # Selected
        sel_mem = getattr(self.engine.mmu_selected, 'physical_memory', [])
        sel_clock = getattr(self.engine.mmu_selected, 'clock', 0)
        for idx in range(min(100, len(self.sel_ram_cells))):
            cell = self.sel_ram_cells[idx]
            page = sel_mem[idx] if idx < len(sel_mem) else None
            if page is None:
                cell.setStyleSheet("background-color: #e0e0e0; border: 1px solid #bdbdbd;")
                cell.setToolTip(f"Frame {idx}: vacío")
            else:
                color = self._get_color_for_pid(getattr(page, 'pid', 0))
                hex_color = color.name()
                cell.setStyleSheet(f"background-color: {hex_color}; border: 1px solid #424242;")
                pid = getattr(page, 'pid', '?')
                page_id = getattr(page, 'page_id', '?')
                ptr = getattr(page, 'ptr', '?')
                loaded_time = getattr(page, 'loaded_time', None)
                t_loaded = (sel_clock - loaded_time) if (loaded_time is not None and sel_clock >= loaded_time) else None
                t_loaded_str = f"{t_loaded}s" if t_loaded is not None else "-"
                cell.setToolTip(f"Frame {idx}\nPID: {pid}\nPage: {page_id}\nPtr: {ptr}\nLoaded-T: {t_loaded_str}")

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.simulation_window = None
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
            
            # Mapear nombres del combo a nombres internos
            algorithm_map = {
                "FIFO": "FIFO",
                "Second Chance": "SC",
                "MRU": "MRU",
                "Random": "RND"
            }
            algorithm_name = algorithm_map.get(algorithm, "FIFO")
            
            if file_path:
                if not os.path.exists(file_path):
                    QMessageBox.warning(self, "Error", "El archivo seleccionado no existe")
                    return
                # Cargar y parsear operaciones desde archivo
                try:
                    parser = OperationParser()
                    operations = parser.parse_file(file_path)
                    print(f"Cargadas {len(operations)} operaciones desde: {file_path}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"No se pudieron parsear las operaciones: {e}")
                    return
            else:
                gen = OperationGenerator()
                operations = gen.generate_operations(num_processes, num_operations, seed)
                print(f"Generadas {len(operations)} operaciones (seed={seed})")
                
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
            
            engine = SimulationEngine(operations, algorithm_name, seed)
            
            self.simulation_window = SimulationWindow(engine, self)
            self.simulation_window.show()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al iniciar simulación: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())
