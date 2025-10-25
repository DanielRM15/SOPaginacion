# SOPaginacion

Simulador de Algoritmos de Paginación para Sistemas Operativos.

## Instalación

### Instalar PySide6

```bash
pip install PySide6
```

## Desarrollo de GUI

### Abrir Qt Designer

Qt Designer se instala automáticamente con PySide6.

```bash
pyside6-designer
```

### Compilar archivos .ui a Python

Después de editar archivos `.ui` en Qt Designer, se deben compilar:

```bash
pyside6-uic gui/mainMenu.ui -o gui/mainMenu_ui.py
pyside6-uic gui/simulation.ui -o gui/simulation_ui.py
```

## Ejecutar

```bash
python main.py
```

