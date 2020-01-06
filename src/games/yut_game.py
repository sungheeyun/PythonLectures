from random import choice
from games.yut_set import YutSet

from matplotlib import pyplot as plt


BT_char_list = [("T", "B") if idx else ("T", "BB") for idx in range(4)]


def throw_yuts():
    bit_list = [choice((0, 1)) for idx in range(4)]
    print(" ".join([BT_char_list[idx][bit] for idx, bit in enumerate(bit_list)]))
    return (sum(bit_list) - 1) % 5 + 1, (sum(bit_list) == 1 and bit_list[0] > 0)


if __name__ == "__main__":
    figure, axis = plt.subplots()

    yut_set: YutSet = YutSet(axis)

    first: bool = True
    count = 0
    while not input("throw! "):
        yut_set.throw()
        count += 1
        axis.set_title(count)
        figure.canvas.draw()
        figure.canvas.flush_events()

        if first:
            figure.show()
        first = False
