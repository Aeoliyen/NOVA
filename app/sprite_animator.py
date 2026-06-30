from PySide6.QtCore import QTimer


class SpriteAnimator:

    def __init__(self, label, loader):
        self.label = label
        self.loader = loader

        self.frames = []
        self.index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_frame)

    def play(self, animation, fps=8):

        self.frames = self.loader.load(animation)
        self.index = 0

        if len(self.frames) == 0:
            self.label.setText(f"NOVA\n{animation}")
            self.timer.stop()
            return

        self.label.setPixmap(self.frames[0])
        self.timer.start(int(1000 / fps))

    def next_frame(self):

        if len(self.frames) == 0:
            return

        self.index += 1

        if self.index >= len(self.frames):
            self.index = 0

        self.label.setPixmap(self.frames[self.index])