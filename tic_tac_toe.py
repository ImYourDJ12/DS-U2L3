from random import choice


class TicTacToe:
  # Initializes class
  def __init__(self):
    self.__board = self.__board()
    self.__turn = choice(["X","O"])
    self.num = 0

  # Places the board numbers into a printable string
  def __str__(self):
    out = f" {self.__board[0][0][0]} | {self.__board[0][1][0]} | {self.__board[0][2][0]}\n {'-'*10}\n"
    out2 = f" {self.__board[1][0][0]} | {self.__board[1][1][0]} | {self.__board[1][2][0]}\n {'-'*10}\n"
    out3 = f" {self.__board[2][0][0]} | {self.__board[2][1][0]} | {self.__board[2][2][0]}\n"
    return out + out2 + out3

  # Holds and creates the board
  def __board(self):
    board = [[" "],[" "],[" "]],[[" "],[" "],[" "]],[[" "],[" "],[" "]]
    return board

  # Checks if there is three in a row anywhere
  def __check_win(self):
    # i am so sorry
    diag1 = [self.__board[0][0][0], self.__board[1][1][0], self.__board[2][2][0]]
    diag2 = [self.__board[2][0][0], self.__board[1][1][0], self.__board[0][2][0]]
    row1 = [self.__board[0][0][0], self.__board[0][1][0], self.__board[0][2][0]]
    row2 = [self.__board[1][0][0], self.__board[1][1][0], self.__board[1][2][0]]
    row3 = [self.__board[2][0][0], self.__board[2][1][0], self.__board[2][2][0]]
    col1 = [self.__board[0][0][0], self.__board[1][0][0], self.__board[2][0][0]]
    col2 = [self.__board[0][1][0], self.__board[1][1][0], self.__board[2][1][0]]
    col3 = [self.__board[0][2][0], self.__board[1][2][0], self.__board[2][2][0]]

    # diag check
    if diag1[0]=="X" and diag1[1]=="X" and diag2[2]=="X" or diag2[0]=="X" and diag2[1]=="X" and diag2[2]=="X":
      return True
    elif diag1[0]=="O" and diag1[1]=="O" and diag1[2]=="O" or diag2[0]=="O" and diag2[1]=="O" and diag2[2]=="O":
      return True
    # row check
    elif row1[0]=="X" and row1[1]=="X" and row1[2]=="X" or row1[0]=="O" and row1[1]=="O" and row1[2]=="O":
      return True
    elif row2[0]=="X" and row2[1]=="X" and row2[2]=="X" or row2[0]=="O" and row2[1]=="O" and row2[2]=="O":
      return True
    elif row3[0]=="X" and row3[1]=="X" and row3[2]=="X" or row3[0]=="O" and row3[1]=="O" and row3[2]=="O":
      return True
    # col check
    elif col1[0]=="X" and col1[1]=="X" and col1[2]=="X" or col1[0]=="O" and col1[1]=="O" and col1[2]=="O":
      return True
    elif col2[0]=="X" and col2[1]=="X" and col2[2]=="X" or col2[0]=="O" and col2[1]=="O" and col2[2]=="O":
      return True
    elif col3[0]=="X" and col3[1]=="X" and col3[2]=="X" or col3[0]=="O" and col3[1]=="O" and col3[2]=="O":
      return True

    else:
      if self.__turn == "X":
        self.__turn = "O"
      elif self.__turn == "O":
        self.__turn = "X"
      return False

  def place_token(self, placement, places):
    dict = {"1":self.__board[0][0],"2":self.__board[0][1],"3":self.__board[0][2],
            "4":self.__board[1][0],"5":self.__board[1][1],"6":self.__board[1][2],
            "7":self.__board[2][0],"8":self.__board[2][1],"9":self.__board[2][2]}
    if dict[placement] == "X":
      return False
    elif dict[placement] == "O":
      return False
    dict[placement].clear()
    dict[placement].append(self.__turn)
    winner = self.__check_win()
    if winner == True:
      return True

  def is_winner(self):
    out = f"Player {self.__turn} wins"
    return out