import sys

from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont

from animation_controller import AnimationController
from sprite_loader import SpriteLoader
from sprite_animator import SpriteAnimator


class NovaWindow(QLabel):
    def __init__(self):
        super().__init__()

        self.anim = AnimationController()
        self.loader = SpriteLoader()
        self.sprite = SpriteAnimator(self, self.loader)

        self.x_dir = 1

        self.setWindowTitle("NOVA")
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont("Arial", 18))
        self.setFixedSize(180, 180)
        self.setStyleSheet(
            "color: white;"
            "background: rgba(0,0,0,0);"
        )

        self.setWindowFlags(
            Qt.FramelessWindowHint
            | Qt.WindowStaysOnTopHint
            | Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.move(300, 300)

        self.setText(f"NOVA\n{self.anim.current()}")

        self.move_timer = QTimer(self)
        self.move_timer.timeout.connect(self.walk)
        self.move_timer.start(30)

        self.anim_timer = QTimer(self)
        self.anim_timer.timeout.connect(self.change_animation)
        self.anim_timer.start(2000)

    def walk(self):
        screen = QApplication.primaryScreen().availableGeometry()

        x = self.x() + self.x_dir * 2

        if x <= 0:
            self.x_dir = 1

        if x + self.width() >= screen.width():
            self.x_dir = -1

        self.move(x, self.y())

    def change_animation(self):
        name = self.anim.next()
        self.setText(f"NOVA\n{name}")
        self.sprite.play(name)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    nova = NovaWindow()
    nova.show()

    sys.exit(app.exec())