from PySide6.QtWidgets import QMessageBox


def ask_save_generated(parent=None) -> bool:
    """Show a Spanish Yes/No dialog asking whether to save generated instructions.

    Returns True if the user clicked "Si", False otherwise.
    """
    msg = QMessageBox(parent)
    msg.setWindowTitle("Guardar instrucciones")
    msg.setText("¿Desea guardar las instrucciones generadas en un archivo?")
    si_btn = msg.addButton("Si", QMessageBox.AcceptRole)
    no_btn = msg.addButton("No", QMessageBox.RejectRole)
    msg.setDefaultButton(si_btn)
    msg.exec()
    clicked = msg.clickedButton()
    return clicked is not None and clicked.text() == "Si"
