#!/usr/bin/env python
from brain_games.games.func_games import *
from brain_games.cli import welcome_user


def task_round():
    count_number_print_in_task = 10
    start_position = get_random_int(1, 50)
    step = get_random_int(1, 5)
    end_position = start_position + (count_number_print_in_task * step)
    unknown_number = get_random_int(1, count_number_print_in_task)
    true_answer = 0
    question = ""

    interaction_print = 0
    for index in range(start_position, end_position):
        if interaction_print == unknown_number:
            question += '.. '
            true_answer = start_position
        elif index == start_position:
            question += f'{index} '
        else:
            continue
        start_position = start_position + step
        interaction_print += 1

    print(f'Question: {question} ')
    print('Your answer: ', end='')
    return str(true_answer)


def task_game():
    print('What number is missing in the progression?')


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
