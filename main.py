import datetime
from result import Result
import random

secret_num = str(random.randint(1, 50))
date = datetime.datetime.now()


def game():
    username = input("What is your username: ").capitalize()
    attempts = 0

    while True:

        user_guess = input("Guess the secret number between 1 and 100: ")
        attempts += 1

        if user_guess == secret_num:
            print("you guessed it right!!!")
            print(f"Secret number was: {secret_num}")
            result = Result(attempts, username, str(date))
            break
        elif user_guess > secret_num:
            print("Too high, try a little smaller..")
        elif user_guess < secret_num:
            print("Too small, try a little higher..")

    return result


with open("results.json", "w") as results_data:
    results_data.write(str(game().__dict__))
