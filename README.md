# SOPaginacion

Simulador de Algoritmos de Paginación para Sistemas Operativos.

## Instalación

### 1. Instalar Python y pip

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
```

### 2. Instalar dependencias necesarias para PySide6

```bash
sudo apt install \
    libxcb-xinerama0 libxcb-cursor0 libxkbcommon-x11-0 \
    libxcb-xinput0 libxcb-icccm4 -y
```

### 3. Crear entorno virtual e instalar dependencias

```bash
cd <ruta-del-proyecto>
python3 -m venv venv
source venv/bin/activate
pip install PySide6
```

## Desarrollo de GUI

### 1. Abrir Qt Designer

Qt Designer se instala automáticamente con PySide6.

```bash
pyside6-designer
```
### 2. Compilar archivos .ui a Python

Después de editar archivos .ui en Qt Designer, se compilan con:

```bash
pyside6-uic gui/mainMenu.ui -o gui/mainMenu_ui.py
pyside6-uic gui/simulationWindow.ui -o gui/simulationWindow_ui.py
```

## Ejecución

Activar el entorno virtual y ejecutar:

```bash
source venv/bin/activate
python3 main.py
```



