#!/usr/bin/env python
from brain_games.cli import welcome_user
import random


def is_even(number) -> bool:
    if number % 2 == 0:
        return True
    return False


def task_raund():
    number = random.randint(1, 29)
    print('Question:', number)
    print('Your answer: ', end='')
    return number


def task_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def result_game(count_question, gamer_name):
    if count_question == 3:
        print(f'Congratulations, {gamer_name}!')
    else:
        print('You lose!')


def is_correct_answer(answer, task):
    if answer == 'yes' and is_even(task):
        return True
    elif answer == 'no' and not is_even(task):
        return True
    else:
        return False


def get_right_answer(task):
    if is_even(task):
        return 'Yes'
    else:
        return 'No'


def get_message_raund(result_round, gamer_answer, correct_answer, gamer_name):
    if result_round:
        print('Correct!')
    else:
        print(f'\'{gamer_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
        print(f'Let\'s try again, {gamer_name}!')



def main():
    name = welcome_user()
    task_game()
    count_question = 0

    while count_question != 3:
        number = task_raund()
        answer = input()
        correct_answer = get_right_answer(number)
        result_round = is_correct_answer(answer, number)

        if result_round:
            get_message_raund(result_round, answer, correct_answer, name)
        else:
            get_message_raund(result_round, answer, correct_answer, name)
            break

        count_question += 1

    result_game(count_question, name)


if __name__ == '__main__':
    main()
