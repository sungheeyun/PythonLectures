from typing import List
from random import choice

from matplotlib.axes import Axes

from games.yut import Yut


class YutSet:
    num_yuts: int = 4

    draw_args: tuple = ('k-',)

    def __init__(self, axis: Axes):
        self.yut_list: List[Yut] = [Yut(idx) for idx in range(YutSet.num_yuts)]
        self.axis: Axes = axis

    def throw(self):
        self.axis.clear()
        back_idx: int = choice(range(len(self.yut_list)))
        for idx, yut in enumerate(self.yut_list):
            yut.throw(idx == back_idx)
            yut.draw(self.axis)

        self.axis.axis("off")
        self.axis.axis("equal")
