from typing import Tuple
from random import choice

from numpy import ndarray, array, hstack, linspace, cos, sin, pi
from matplotlib.axes import Axes


def get_partial_circle_xy_array(
    center_array: ndarray,
    radius: float,
    start_angle_in_degrees: float = 0,
    end_angle_in_degrees: float = 0,
    num_points: int = 20,
) -> Tuple[ndarray, ndarray]:
    angle_array_in_rad: ndarray = (pi / 180.0) * linspace(start_angle_in_degrees, end_angle_in_degrees, num_points)
    x_array: ndarray = center_array[0] + radius * cos(angle_array_in_rad)
    y_array: ndarray = center_array[1] + radius * sin(angle_array_in_rad)

    return x_array, y_array


class Yut:
    width: float = 1.0
    height: float = 5.0
    corner_radius: float = 0.35
    distance: float = 1.5
    cross_size: float = 0.5
    cross_height: float = 1.5

    quarter_circle_x_array_1: ndarray
    quarter_circle_y_array_1: ndarray

    quarter_circle_x_array_2: ndarray
    quarter_circle_y_array_2: ndarray

    quarter_circle_x_array_3: ndarray
    quarter_circle_y_array_3: ndarray

    quarter_circle_x_array_4: ndarray
    quarter_circle_y_array_4: ndarray

    quarter_circle_x_array_1, quarter_circle_y_array_1 = get_partial_circle_xy_array(
        (width / 2.0 - corner_radius, height / 2.0 - corner_radius), corner_radius, 0.0, 90.0
    )

    quarter_circle_x_array_2, quarter_circle_y_array_2 = get_partial_circle_xy_array(
        (-width / 2.0 + corner_radius, height / 2.0 - corner_radius), corner_radius, 90.0, 180.0
    )

    quarter_circle_x_array_3, quarter_circle_y_array_3 = get_partial_circle_xy_array(
        (-width / 2.0 + corner_radius, -height / 2.0 + corner_radius), corner_radius, 180.0, 270.0
    )

    quarter_circle_x_array_4, quarter_circle_y_array_4 = get_partial_circle_xy_array(
        (width / 2.0 - corner_radius, -height / 2.0 + corner_radius), corner_radius, 270.0, 360.0
    )

    x_list: ndarray = array([0, 1, 1, 0, 0], float) * width - width / 2.0
    y_list: ndarray = array([0, 0, 1, 1, 0], float) * height - height / 2.0

    x_list: ndarray = hstack((
        quarter_circle_x_array_1,
        quarter_circle_x_array_2,
        quarter_circle_x_array_3,
        quarter_circle_x_array_4,
        quarter_circle_x_array_1[:1]
    ))

    y_list: ndarray = hstack((
        quarter_circle_y_array_1,
        quarter_circle_y_array_2,
        quarter_circle_y_array_3,
        quarter_circle_y_array_4,
        quarter_circle_y_array_1[:1]
    ))

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

        if self.result == 0:
            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_1, *args, **kwargs)
            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_2, *args, **kwargs)

            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_1 + Yut.cross_height, *args, **kwargs)
            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_2 + Yut.cross_height, *args, **kwargs)

            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_1 - Yut.cross_height, *args, **kwargs)
            axis.plot(Yut.x_cross_list + x_shift, Yut.y_cross_list_2 - Yut.cross_height, *args, **kwargs)
        else:
            if self.back:
                axis.plot(array([-1, 1], float) * Yut.width / 2 + x_shift, [0.0, 0.0], *args, **kwargs)
