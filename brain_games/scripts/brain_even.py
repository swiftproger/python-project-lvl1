#!/usr/bin/env python
from brain_games.cli import welcome_user
import random


def is_even(number) -> bool:
    if number % 2 == 0:
        return True
    return False


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count_question = 0

    while count_question != 3:
        number = random.randint(1, 29)
        print('Question:', number)
        print('Your answer: ', end='')
        answer = input()

        if (answer == 'yes' and is_even(number)) or (answer == 'no' and not is_even(number)):
            print('Correct!')
        elif answer == 'yes' and not is_even(number):
            print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            break
        elif answer == 'no' and is_even(number):
            print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
            break
        else:
            print('Answer only \'yes\' or \'no\'')
            break
        count_question += 1

    if count_question == 3:
        print(f'Congratulations, {name}!')
    else:
        print('You lose!')


if __name__ == '__main__':
    main()
