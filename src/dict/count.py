
import random

if __name__ == "__main__":

    N = 10000

    num_rocks = 0
    num_scissors = 0
    num_papers = 0

    for idx in range(N):
        selection = random.choice(['rock', 'scissors', 'paper'])

        if selection == 'rock':
            num_rocks += 1
        elif selection == 'scissors':
            num_scissors += 1
        else:
            num_papers += 1

    print("num_rocks:", num_rocks/N)
    print("num_scissors:", num_scissors/N)
    print("num_papers:", num_papers/N)

