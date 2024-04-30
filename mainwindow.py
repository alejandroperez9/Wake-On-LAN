
#--- ALEJANDRO PEREZ ARANDA
#--- WAKE ON LAN

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from wakeonlan import send_magic_packet

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WakeOnLAN")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.mac_label = QLabel("Dirección MAC:")
        self.mac_input = QLineEdit()
        layout.addWidget(self.mac_label)
        layout.addWidget(self.mac_input)

        self.ip_label = QLabel("Dirección Broadcast:")
        self.ip_input = QLineEdit()
        layout.addWidget(self.ip_label)
        layout.addWidget(self.ip_input)

        self.send_button = QPushButton("Activar PC")
        self.send_button.clicked.connect(self.send_wol)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def send_wol(self):
        mac = self.mac_input.text()
        ip = self.ip_input.text()

        try:
            send_magic_packet(mac, ip_address=ip)
            QMessageBox.information(self, "Éxito", "Paquete WakeOnLAN enviado con éxito.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo enviar el paquete WakeOnLAN: {str(e)}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
