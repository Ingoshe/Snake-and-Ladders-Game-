import random

class SnakeAndLadders:
    def __init__(self):
        self.board = [[0 for _ in range(10)] for _ in range(10)]
        self.snakes = [(1, 38), (4, 2), (8, 31), (17, 7), (20, 25), (22, 8), (28, 3), (36, 1), (43, 19), (50, 46)]
        self.ladders = [(1, 4), (4, 9), (7, 14), (16, 24), (21, 28), (34, 50), (42, 68), (44, 67), (49, 51), (56, 59)]
        self.players = {}

    def get_position(self, player):
        return self.players[player]

    def dice_roll(self, player):
        roll = random.randint(1, 6)
        position = self.get_position(player)
        self.players[player] = (position + roll) % 100
        return self.players[player]

    def snake_or_ladder(self, player):
        position = self.get_position(player)
        for snake in self.snakes:
            if snake[0] == position:
                self.players[player] = snake[1]
                print(f"Player {player} landed on the head of a snake. Moved to {snake[1]}")
                return
        for ladder in self.ladders:
            if ladder[0] == position:
                self.players[player] = ladder[1]
                print(f"Player {player} landed on the bottom of a ladder. Moved to {ladder[1]}")
                return

    def play(self):
        for player in self.players:
            print(f"Player {player} is at position {self.get_position(player)}")
            self.dice_roll(player)
            self.snake_or_ladder(player)
            print(f"Player {player} rolled a {random.randint(1, 6)} and is now at position {self.get_position(player)}")
        winner = min(self.players, key=self.players.get)
        print(f"Player {winner} wins the game!")

    def main(self):
        num_players = int(input("Enter the number of players (1-4): "))
        for i in range(num_players):
            name = input(f"Enter the name of player {i+1}: ")
            self.players[name] = 0
        self.play()

if __name__ == "__main__":
    game = SnakeAndLadders()
    game.main()
