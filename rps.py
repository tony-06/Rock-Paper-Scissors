import random
import sys


class Player:
    def __init__(self):
        self.score = 0
        self.moves = ["rock", "paper", "scissors"]

    def get_move(self):
        raise NotImplementedError()

    def add_score(self):
        self.score += 1


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer"

    def get_move(self):
        return random.choice(self.moves)


class HumanPlayer(Player):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.moves = ["rock", "paper", "scissors", "quit"]

    def get_move(self):
        move = input("Enter 'rock', 'paper', or 'scissors', or 'quit' to exit: ")
        if move not in self.moves:
            print("Invalid move, please try again.")
            return self.get_move()
        else:
            return move


def initialize_game():
    name = input("Enter your name: ")
    human_player = HumanPlayer(name)
    computer_player = ComputerPlayer()
    return human_player, computer_player


def print_score(human_player, computer_player):
    print(f"Score: {human_player.name}: {human_player.score}, {computer_player.name}: {computer_player.score}")


def determine_winner(human_move, computer_move):
    if human_move == computer_move:
        return "tie"
    elif human_move == "rock" and computer_move == "scissors":
        return "human"
    elif human_move == "paper" and computer_move == "rock":
        return "human"
    elif human_move == "scissors" and computer_move == "paper":
        return "human"
    else:
        return "computer"


def play_round(human_player, computer_player):
    human_move = human_player.get_move()
    computer_move = computer_player.get_move()

    if human_move == "quit":
        print("Game Over")
        print_score(human_player, computer_player)
        sys.exit()

    print(f"{human_player.name} chose {human_move}")
    print(f"{computer_player.name} chose {computer_move}")

    winner = determine_winner(human_move, computer_move)
    if winner == "tie":
        print("It's a tie!")
    elif winner == "human":
        print(f"{human_player.name} wins!")
        human_player.add_score()
    else:
        print(f"{computer_player.name} wins!")
        computer_player.add_score()

    # Display the score
    print_score(human_player, computer_player)


def main():
    human_player, computer_player = initialize_game()

    # Play the game until the user quits
    while True:
        play_round(human_player, computer_player)


if __name__ == "__main__":
    main()
