from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont
import sys


class NovaWindow(QLabel):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NOVA")
        self.setText("NOVA\nidle")
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("Arial", 18))
        self.setFixedSize(180, 180)
        self.setStyleSheet(
            "background: rgba(30,30,30,170); color: white; border-radius: 30px;"
        )
        self.setWindowFlags(
            Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool
        )
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.x_dir = 1
        self.move(300, 300)

        self.timer = QTimer()
        self.timer.timeout.connect(self.walk)
        self.timer.start(30)

    def walk(self):
        x = self.x() + self.x_dir * 2
        y = self.y()
        screen = QApplication.primaryScreen().availableGeometry()

        if x < 0 or x + self.width() > screen.width():
            self.x_dir *= -1

        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    nova = NovaWindow()
    nova.show()
    sys.exit(app.exec())
