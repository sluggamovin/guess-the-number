import random as rd

counter = 0
guesses_made = []
magic_number = rd.randint(1, 10)
print(magic_number)

guess = int(input("Guess a number between 1 and 10: "))
guesses_made.append(guess)
counter += 1

while guess != magic_number and counter < 5:
  print("You already guessed: %s" % guesses_made)
  guess = int(input("Guess a number between 1 and 10: "))
  guesses_made.append(guess)
  
  counter += 1
  
  if guess == magic_number:
     print("You win!")
  else:
     print("Incorrect!")
     
if counter >= 5:
  print("You lose!")
