#This code was created as an example of using TechTeacher https://github.com/MiliTenorio/TechTeacher
#https://replit.com/@mitenorio/GuessTheNumber
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10.")

while True:
  guess = int(input("Take a guess: "))

  if guess == secret_number:
      print("Congratulations! You guessed it!")
      break  # This exits the loop
  elif guess < secret_number:
      print("Too low! Try again.")
  else:
      print("Too high! Try again.")
