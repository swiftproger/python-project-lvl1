#!/usr/bin/env python
from math import gcd
from brain_games.cli import welcome_user
from brain_games.games.func_games \
    import result_game, get_message_round, get_random_int, is_correct_answer


def task_round():
    number1 = get_random_int()
    number2 = get_random_int()

    print(f'Question: {number1} {number2}')
    print('Your answer: ', end='')
    return str(gcd(number1, number2))


def task_game():
    print('Find the greatest common divisor of given numbers.')


def main():
    name = welcome_user()
    task_game()
    count_question = 0

    while count_question != 3:
        correct_answer = task_round()
        answer = input()
        result_round = is_correct_answer(answer, correct_answer)
        get_message_round(result_round, answer, correct_answer, name)

        if result_round:
            count_question += 1
        else:
            break

    result_game(count_question, name)


if __name__ == '__main__':
    main()
