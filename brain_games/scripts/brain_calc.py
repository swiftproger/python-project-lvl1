#!/usr/bin/env python
from brain_games.games.func_games import result_game, get_message_round, get_random_int, is_correct_answer
from brain_games.cli import welcome_user


def multiply_task(num1, num2):
    return num1 * num2


def deduction_task(num1, num2):
    return num1 - num2


def sum_task(num1, num2):
    return num1 + num2


def task_round(round):
    number1 = get_random_int()
    number2 = get_random_int()

    if round == 0:
        print(f'Question: {number1} + {number2}')
        print('Your answer: ', end='')
        return str(sum_task(number1, number2))
    elif round == 1:
        print(f'Question: {number1} - {number2}')
        print('Your answer: ', end='')
        return str(deduction_task(number1, number2))
    elif round == 2:
        print(f'Question: {number1} * {number2}')
        print('Your answer: ', end='')
        return str(multiply_task(number1, number2))


def task_game():
    print('What is the result of the expression?')


def main():
    name = welcome_user()
    task_game()
    count_question = 0

    while count_question != 3:
        correct_answer = task_round(count_question)
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
