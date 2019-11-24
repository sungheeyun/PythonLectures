
import pandas
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":

    data_frame = pandas.DataFrame(
        np.array([[3423, 1323, 4563], [3523, 3432, 3454]]).T,
        index=['Honda', 'Benz', 'Ford'],
        columns=['market share', 'company value']
    )
    print(data_frame)

    data_frame.plot.bar()
    data_frame.plot.pie(y='market share')
    plt.show()





