from random import random

D = 2  # unit circle
NUM_GAMES = 10**10


def get_rand():
    return random() * D - 1


def trial():
    return get_rand(), get_rand()


def play_game():
    score = 0   # we get 1 for just playing
    r_squared = 0.5 * D  # 1

    while r_squared >= 0:
        x, y = trial()
        score += 1
        r_squared -= x**2 + y**2

    return score


def main():
    total = 0

    for i in range(NUM_GAMES):
        score = play_game()
        total += score

    print(f'Sample mean: {total / NUM_GAMES}')


main()

