from player import Player
import time

class Human(Player):
    def __init__(self) -> None:
        super().__init__()
        time.sleep(.5)
        self.name = input("Enter Player one's name: ")
    
    def choose_gesture(self):
            print('')
            time.sleep(.5)
            print('(0)Rock', '(1)Paper', '(2)Scissors', '(3)Lizard', '(4)Spock')
            gesture_index = int(input(f"{self.name}, enter a number between 0 and 4: "))
            valid_indexes_list = [0, 1, 2, 3, 4]
            while valid_indexes_list.count(gesture_index) == 0:
                print('Invalid entry. Try again.')
                gesture_index = int(input(f"{self.name}, enter a number between 0 and 4: "))
                
            self.chosen_gesture = self.gestures_list[gesture_index]
            time.sleep(.5)
            return self.chosen_gesture


                