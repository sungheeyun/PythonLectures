from numpy import array, ndarray

if __name__ == "__main__":
    x_array: ndarray = array([1, 2, 4, 8, 16], float)
    y_array: ndarray = array([34046995, 92207123, 281218384, 1004214144, 3754343140], float)

    for idx, y in enumerate(y_array[:-1]):
        print(y_array[idx + 1] / y)
