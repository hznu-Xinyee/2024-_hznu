from PyQt5.QtWidgets import QMessageBox


def warning(title: str, text: str, buttons=QMessageBox.Ok):
    msgbox = QMessageBox()
    msgbox.setIcon(QMessageBox.Warning)
    msgbox.setWindowTitle(title)
    msgbox.setText(text)
    msgbox.setStandardButtons(buttons)
    reply = msgbox.exec()
    return reply
