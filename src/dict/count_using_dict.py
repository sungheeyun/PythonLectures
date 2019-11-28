
import random

if __name__ == "__main__":

    N = 10000

    count_dict = {'rock': 0, 'scissors': 0, 'paper': 0}

    for idx in range(N):
        selection = random.choice(['rock', 'scissors', 'paper'])
        count_dict[selection] += 1

    print("num_rocks:", count_dict['rock']/N)
    print("num_scissors:", count_dict['scissors']/N)
    print("num_papers:", count_dict['paper']/N)

