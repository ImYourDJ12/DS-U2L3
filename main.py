# Devon Taylor
# U2L3
# DS
# 9/26/24

from tic_tac_toe import TicTacToe
from random import choice
from time import sleep
import os

def turn(out,places):
  print(out)
  print("   1 2 3\n   4 5 6\n   7 8 9\n")
  placement = input("Enter your move(1-9): ")
  valid = False
  while valid == False:
    try:
      int(placement)
      if placement in places:
        valid = True
      else:
        print("That is not a valid number")
        placement = input("Enter a valid number: ")
    except:
      print("That is not a valid number")
      placement = input("Enter a valid number: ")
  place = out.place_token(placement,places)
  if place == True:
    return True
  return placement
  

def compTurn(out,places):
  if len(places) == 0:
    return False
  else:
    placement = choice(places)
    places.remove(placement)
    place = out.place_token(placement,places)
    if place == True:
      return True
    return placement

def main():
  places = ["1","2","3","4","5","6","7","8","9"]
  out = TicTacToe()
  winner = False
  while winner == False:
    placement = turn(out,places)
    if placement == True:
      winner = True
      break
    else:
      places.remove(placement)

    sleep(0.5)
    compPlace = compTurn(out,places)

    if compPlace == False:
      break
    elif compPlace == True:
      winner = True
    os.system('cls' if os.name == 'nt' else 'clear')

  if winner == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(out)
    text = out.is_winner()
    print(text)
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(out)
    print("Draw")

if __name__ == "__main__":
  main()