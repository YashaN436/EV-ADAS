import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QVBoxLayout,
    QGridLayout
)

from PyQt5.QtCore import Qt


class EVDashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("EV + ADAS Dashboard")

        self.setGeometry(200, 100, 900, 600)

        self.create_dashboard()

    def create_dashboard(self):

        main_layout = QVBoxLayout()

        # Title
        title = QLabel("⚡ ELECTRIC VEHICLE DASHBOARD")
        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            padding: 20px;
        """)

        main_layout.addWidget(title)

        # Grid
        grid = QGridLayout()

        self.speed_label = QLabel("🚗 Speed\n65 km/h")
        self.battery_label = QLabel("🔋 Battery\n82 %")
        self.voltage_label = QLabel("⚡ Voltage\n398 V")
        self.temperature_label = QLabel("🌡️ Temperature\n42 °C")
        self.distance_label = QLabel("📍 Distance\n12.5 km")
        self.adas_label = QLabel("🟢 ADAS\nSYSTEM SAFE")

        labels = [
            self.speed_label,
            self.battery_label,
            self.voltage_label,
            self.temperature_label,
            self.distance_label,
            self.adas_label
        ]

        for label in labels:

            label.setAlignment(Qt.AlignCenter)

            label.setStyleSheet("""
                font-size: 20px;
                padding: 30px;
                border: 2px solid gray;
                border-radius: 10px;
            """)

        grid.addWidget(self.speed_label, 0, 0)
        grid.addWidget(self.battery_label, 0, 1)

        grid.addWidget(self.voltage_label, 1, 0)
        grid.addWidget(self.temperature_label, 1, 1)

        grid.addWidget(self.distance_label, 2, 0)
        grid.addWidget(self.adas_label, 2, 1)

        main_layout.addLayout(grid)

        # Warning
        warning = QLabel("🟢 SYSTEM SAFE")

        warning.setAlignment(Qt.AlignCenter)

        warning.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            padding: 20px;
        """)

        main_layout.addWidget(warning)

        self.setLayout(main_layout)


app = QApplication(sys.argv)

window = EVDashboard()

window.show()

sys.exit(app.exec_())
