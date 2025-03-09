# Number guessing game

# generate random number
import random
number = random.randint(0, 100)

# welcome message
print('''Welcome to the Number Guessing Game!
You've 5 lives.''')

i = 1
while i <= 5:
  print(f"Try number {i}")
  try:
    guess_number = int(input("Guess a number between 0 to 100. "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue
  # hints for engagment
  if guess_number == number:
    print("Congratulations! Your guess is right.")
    break
  elif guess_number > number:
    print("Too high! Try again.")
  elif guess_number < number:
    print("Too low! Try again.")
  i+=1
else:
  print("Better luck next time.")
