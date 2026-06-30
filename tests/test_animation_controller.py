import unittest

from app.animation_controller import AnimationController


class AnimationControllerTests(unittest.TestCase):
    def test_initial_state_and_next_state(self):
        controller = AnimationController()

        self.assertEqual(controller.current(), "idle")
        self.assertEqual(controller.next(), "happy")
        self.assertEqual(controller.current(), "happy")


if __name__ == "__main__":
    unittest.main()
