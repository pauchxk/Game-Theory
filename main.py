#this program implements the functionality of the prisoner's dilemma, allowing two different strategies to be imported and used to play against each other.


#imports#
import random


#game#
class PrisonerDilemma:

    def __init__(self):
        self.player1_points = 0
        self.player2_points = 0
        self.player1_c = 0
        self.player2_c = 0
        self.player1_d = 0
        self.player2_d = 0

    
    def run_game(self, status1, status2):

        for _ in range(200):
            stat1 = status1()
            stat2 = status2()

            if stat1 == 0 and stat2 == 0:
                print('C    C')
                self.player1_points += 3
                self.player2_points += 3

                self.player1_c += 1
                self.player2_c += 1

            elif stat1 == 1 and stat2 == 1:
                print('D    D')
                self.player1_points += 1
                self.player2_points += 1

                self.player1_d += 1
                self.player2_d += 1

            elif stat1 == 0 and stat2 == 1:
                print('C    D')
                self.player2_points += 5

                self.player1_c += 1
                self.player2_d += 1

            elif stat1 == 1 and stat2 == 0:
                print('D    C')
                self.player1_points += 5

                self.player1_d += 1
                self.player2_c += 1


        if self.player1_points == self.player2_points:
            return f"No winner - Player 1 scored {self.player1_points} and Player 2 scored {self.player2_points}."
        elif self.player1_points > self.player2_points:
            return f"Winner is Player 1 with {self.player1_points}, Player 2 scored {self.player2_points}."
        elif self.player1_points < self.player2_points:
            return f"Winner is Player 2 with {self.player2_points}, Player 1 scored {self.player1_points}."


#temp players#
def status1():
    return random.randint(0,1)

def status2():
    return random.randint(0,1)

game = PrisonerDilemma()
print(game.run_game(status1, status2))