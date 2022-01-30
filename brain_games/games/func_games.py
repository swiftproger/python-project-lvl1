#!/usr/bin/env python
import random


def get_random_int():
    return random.randint(1, 29)


def result_game(count_question, gamer_name):
    if count_question == 3:
        print(f'Congratulations, {gamer_name}!')
    else:
        print('You lose!')


def get_message_round(result_round, gamer_answer, correct_answer, gamer_name):
    if result_round:
        print('Correct!')
    else:
        print(f'\'{gamer_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
        print(f'Let\'s try again, {gamer_name}!')


def main():
    print('Модуль не предназначен для самостоятельного запуска')


if __name__ == '__main__':
    main()