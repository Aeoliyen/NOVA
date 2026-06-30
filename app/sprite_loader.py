from pathlib import Path
from PySide6.QtGui import QPixmap

class SpriteLoader:
    def __init__(self, base_path="assets/sprites/nova"):
        self.base_path = Path(base_path)
        self.cache = {}

    def load(self, animation):
        if animation in self.cache:
            return self.cache[animation]

        folder = self.base_path / animation
        frames = []

        if folder.exists():
            for file in sorted(folder.glob("*.png")):
                frames.append(QPixmap(str(file)))

        self.cache[animation] = frames
        return frames