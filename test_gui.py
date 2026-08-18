import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("EV-ADAS GUI Test")
window.resize(500, 300)

label = QLabel("🚗 EV-ADAS GUI is working!", window)
label.move(120, 130)

window.show()

sys.exit(app.exec_())
