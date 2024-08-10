"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""
import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value

    def roll_die(self):
        new_value = random.randint(1, 6)
        self._value = new_value


class Player:

    def __init__(self, die: Die, is_computer: bool = False, score=10):
        self.is_computer = is_computer
        self._die = die
        self.score = score

    @property
    def counter(self):
        return self._die.value

    def __eq__(self, other):  #==
        if other is None:
            return False
        elif isinstance(other, str):
            return self.name == other

    def increment(self):
        self.score += 1

    def decremnt(self):
        self.score -= 1

    def roll_die(self) -> int:
        self._die.roll_die()
        return self._die.value


class DiceGame:
    def __init__(self, human: Player, computer: Player):
        self.human = human
        self.computer = computer

    def start_game(self):
        print()
        while (True):
            self.play_round()
            if (self.check_end_game() != None):
                break

    def welcome_game(self):
        print("welcome to new round")
        input("please press Enter to start your turn")

    def show_dice(self, result_die_human, result_die_computer):
        print(f'computer has {result_die_computer} in the dice')
        print(f'human has {result_die_human} in the dice\n')

    def show_counter(self):
        print(f'computer has {computer.score} score')
        print(f'human has {human.score} score')

    def update_counter(self, looser, winner):
        winner.increment()
        looser.decremnt()

    def play_round(self):
        self.welcome_game()

        result_die_human = self.human.roll_die()
        result_die_computer = self.computer.roll_die()

        if result_die_human > result_die_computer:
            print("human won this round\n")
            self.update_counter(looser=self.computer, winner=self.human)
        else:
            print("computer won this round\n")
            self.update_counter(looser=self.human, winner=self.computer)

        self.show_dice(result_die_human, result_die_computer)
        self.show_counter()

        #This method should handle the main round logic. It should welcome the

    ##This method should handle the main round logic. It should welcome the
    #player to the round, roll the dice, determine the winner and loser of the
    #round, update the counters accordingly, and show the values of the
    #counters.

    def check_end_game(self):

        if self.human.counter <= 0:
            return self.computer
        elif self.computer.counter <= 0:
            return self.human
        else:
            return None

    def check_game_over(self, winner):
        if winner.is_computer:
            print("computer won the game\n")
        else:
            print("human won the game\n")



if __name__ == '__main__':
    human_die = Die()
    computer_die = Die()

    human = Player(human_die, False)
    computer = Player(computer_die, True)

    dice_game = DiceGame(human, computer)

    dice_game.start_game()