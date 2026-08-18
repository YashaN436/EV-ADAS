import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel


app = QApplication(sys.argv)

window = QWidget()

window.setWindowTitle("EV-ADAS GUI Test")

window.resize(500, 300)

label = QLabel("EV-ADAS GUI is working!", window)

label.move(150, 130)

window.show()

sys.exit(app.exec())
