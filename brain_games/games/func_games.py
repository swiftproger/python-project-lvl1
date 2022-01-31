#!/usr/bin/env python
import random


def get_random_int(num1=1, num2=5):
    return random.randint(num1, num2)


def result_game(count_question, gamer_name):
    if count_question == 3:
        print(f'Congratulations, {gamer_name}!')


def get_message_round(result_round, gamer_answer, correct_answer, gamer_name):
    if result_round:
        print('Correct!')
    else:
        print(f'\'{gamer_answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.')
        print(f'Let\'s try again, {gamer_name}!')


def is_correct_answer(answer, correct_answer):
    if answer == correct_answer:
        return True
    return False


def main():
    print('Модуль не предназначен для самостоятельного запуска')


if __name__ == '__main__':
    main()
