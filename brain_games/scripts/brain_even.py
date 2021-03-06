#!/usr/bin/env python
from brain_games.cli import welcome_user
from brain_games.games.func_games \
    import result_game, get_message_round, get_random_int


def is_even(number) -> bool:
    if number % 2 == 0:
        return True
    return False


def task_round():
    number = get_random_int()
    print('Question:', number)
    print('Your answer: ', end='')
    return number


def task_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')


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


def main():
    round_count: int = 3
    name = welcome_user()
    task_game()
    count_question = 0

    for _ in range(0, round_count):
        number = task_round()
        answer = input()
        correct_answer = get_right_answer(number)
        result_round = is_correct_answer(answer, number)
        get_message_round(result_round, answer, correct_answer, name)

        if result_round:
            count_question += 1
        else:
            break

    result_game(count_question, name)


if __name__ == '__main__':
    main()
