from random import choice

from numpy import ndarray, array
from matplotlib.axes import Axes


class Yut:
    width: float = 1.0
    height: float = 5.0
    corner_radius: float = .1
    distance: float = 1.5
    cross_size: float = 0.5
    cross_height: float = 1.5

    x_list: ndarray = array([0, 1, 1, 0, 0], float) * width - width / 2.0
    y_list: ndarray = array([0, 0, 1, 1, 0], float) * height - height / 2.0

    x_cross_list: ndarray = array([-1, 1], float) * cross_size / 2.0
    y_cross_list_1: ndarray = array([1, -1], float) * cross_size / 2.0
    y_cross_list_2: ndarray = array([-1, 1], float) * cross_size / 2.0

    def __init__(self, idx: int) -> None:
        self.idx: int = idx
        self.result: int = 0
        self.back: bool = False

    def throw(self, back: bool) -> None:
        self.result = choice((0, 1))
        self.back = back

    def draw(self, axis: Axes, *args, **kwargs) -> None:
        x_shift: float = self.idx * Yut.distance

        axis.plot(Yut.x_list + x_shift, Yut.y_list, *args, **kwargs)

        print(self.result)
        if self.result == 0:
            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_1, *args, **kwargs)
            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_2, *args, **kwargs)

            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_1 + Yut.cross_height, *args, **kwargs)
            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_2 + Yut.cross_height, *args, **kwargs)

            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_1 - Yut.cross_height, *args, **kwargs)
            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_2 - Yut.cross_height, *args, **kwargs)
        else:
            if self.back:
                axis.plot(array([-1, 1], float) * Yut.width/2 + x_shift, [0.0, 0.0], *args, **kwargs)
