from player import Player
import random
import time

class AI(Player):
    def __init__(self) -> None:
        super().__init__()
        time.sleep(.5)
        self.name = input("Enter a name for AI player: ")

    def choose_gesture(self):
        self.chosen_gesture = random.choice(self.gestures_list)
        return self.chosen_gesture