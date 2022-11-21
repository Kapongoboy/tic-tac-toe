from clear import clear
from random import randint
clear()

class TicTacToe:
   def __init__(self) -> None:
      self.players = [" X ", " O "]
      self.input_pos = 0
      self.turn = randint(0, 1)
      self.coordinates = {7:"   ",
                           8:"   ",
                           9:"   ",
                           4:"   ",
                           5:"   ",
                           6:"   ",
                           1:"   ",
                           2:"   ",
                           3:"   ",
                          }
      self.tile = f"{self.coordinates[7]}|{self.coordinates[8]}|{self.coordinates[9]}\n-----------\n{self.coordinates[4]}|{self.coordinates[5]}|{self.coordinates[6]}\n-----------\n{self.coordinates[1]}|{self.coordinates[2]}|{self.coordinates[3]}"
      self.game_over = False

   def play_game(self):
      print(f"It's player {self.players[self.turn]}'s turn")
      self.player_input()
      self.tile = f"{self.coordinates[7]}|{self.coordinates[8]}|{self.coordinates[9]}\n-----------\n{self.coordinates[4]}|{self.coordinates[5]}|{self.coordinates[6]}\n-----------\n{self.coordinates[1]}|{self.coordinates[2]}|{self.coordinates[3]}"
      clear()
      print(self.tile)
      self.game_over = self.check_draw()
      self.game_over = self.win_condi()
      if not self.game_over:
         self.switch_players()
         self.play_game()

   def win_condi(self):
      if self.coordinates[7] == self.players[self.turn] and self.coordinates[8] ==self.players[self.turn] and self.coordinates[9] == self.players[self.turn]:
         print(f"Congrates {self.players[self.turn]} wins")
         return True
      elif self.coordinates[4] == self.players[self.turn] and self.coordinates[5] ==self.players[self.turn] and self.coordinates[6] == self.players[self.turn]:
         print(f"Congrates {self.players[self.turn]} wins")
         return True
      elif self.coordinates[1] == self.players[self.turn] and self.coordinates[2] ==self.players[self.turn] and self.coordinates[3] == self.players[self.turn]:
         print(f"Congrates {self.players[self.turn]} wins")
         return True
      elif self.coordinates[7] == self.players[self.turn] and self.coordinates[4] ==self.players[self.turn] and self.coordinates[1] == self.players[self.turn]:
         print(f"Congrates {self.players[self.turn]} wins")
         return True
      elif self.coordinates[8] == self.players[self.turn] and self.coordinates[5] ==self.players[self.turn] and self.coordinates[2] == self.players[self.turn]:
         print(f"Congrates {self.players[self.turn]} wins")
         return True
      elif self.coordinates[9] == self.players[self.turn] and self.coordinates[6] ==self.players[self.turn] and self.coordinates[3] == self.players[self.turn]:
         print(f"Congrates {self.players[self.turn]} wins")
         return True
      elif self.coordinates[7] == self.players[self.turn] and self.coordinates[5] ==self.players[self.turn] and self.coordinates[3] == self.players[self.turn]:
         print(f"Congrates {self.players[self.turn]} wins")
         return True
      elif self.coordinates[9] == self.players[self.turn] and self.coordinates[5] ==self.players[self.turn] and self.coordinates[1] == self.players[self.turn]:
         print(f"Congrates {self.players[self.turn]} wins")
         return True
      else:
         return False

   def check_draw(self):
      count = 0
      for block in self.coordinates:
         if self.coordinates[block] != "   ":
            count += 1
      if count == 9:
         print("It's a draw")
         return True
      else:
         return False
         

   def switch_players(self):
      if self.turn == 0:
         self.turn = 1
      else:
         self.turn = 0

   def check_input(self, choice):
      count = 0
      for i in range(1, 10):
         if choice != i:
            count += 1
      if count == 9:
         print("Please Enter a valid input")
         return False
      else:
         return True
      
   def player_input(self):
      try:
         self.input_position = int(input())
      except ValueError:
         print("Please enter a valid input")
         self.player_input()
      else:
         if not self.check_input(self.input_position):
            self.player_input()
      self.coordinates[self.input_position] = self.players[self.turn]