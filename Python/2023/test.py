import random

p1_win = 0
p2_win = 0
playerdraw = 0
rounds = 0

def play():
  global rounds
  p1 = random.choice(["rock", "paper", "scissors"])
  p2 = random.choice(["rock", "paper", "scissors"])

  if pdraw(p1, p2):
    print("it's a draw")

  elif p1Win(p1, p2):
      print("player one wins")

  elif p2Win(p1, p2):
      print("player 2 won this round")


def p1Win (p1, p2):
  global p1_win, rounds
  if (p1 == "rock" and p2 == "scissors") or (p1 == "paper" and p2 == "rock") or (p1 == "scissors" and p2 == "paper"):
      p1_win += 1
      rounds +=1
      return True

def p2Win (p1, p2):
  global p2_win, rounds
  if (p1 == "rock" and p2 == "paper") or (p1 == "paper" and p2 == "scissors") or (p1 == "scissors" and p2 == "rock"):
      p2_win += 1
      rounds += 1
      return True 

def pdraw(p1, p2):
    global playerdraw, rounds
    if p1 == p2:
        playerdraw += 1
        rounds += 1
        return True

while rounds < 20:
    play()

print(f"in {rounds} rounds, player1 won {p1_win} games, while player2 won {p2_win} with {playerdraw} draws")