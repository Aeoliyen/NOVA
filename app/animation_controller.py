class AnimationController:
    def __init__(self):
        self.animations = ["idle", "walk", "coffee", "sleep"]
        self.index = 0

    def current(self):
        return self.animations[self.index]

    def next(self):
        self.index = (self.index + 1) % len(self.animations)
        return self.current()