from clear import clear

class TicTacToe:
   def __init__(self) -> None:
      self.icons = ["X", "O"]
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
      clear()
      print(self.tile)
      self.coordinates[int(input())] = " X "
      self.tile = f"{self.coordinates[7]}|{self.coordinates[8]}|{self.coordinates[9]}\n-----------\n{self.coordinates[4]}|{self.coordinates[5]}|{self.coordinates[6]}\n-----------\n{self.coordinates[1]}|{self.coordinates[2]}|{self.coordinates[3]}"
      self.game_over = self.win_condi()
      if not self.game_over:
         self.play_game()

   def win_condi(self):
      if (self.coordinates[7] and self.coordinates[8] and self.coordinates[9]) == " X ":
         print("Congrates X wins")
         return True
      else:
         return False



