class Player:
    def __init__(self) -> None:
        self.name = "player"
        self.gestures_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.num_of_wins = 0
        self.chosen_gesture = self.gestures_list[0]


