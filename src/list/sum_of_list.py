def sum_of_list(my_list):
    res = 0

    for element in my_list:
        res += element

    return res


if __name__ == "__main__":

    your_list = [1, 3, 10, 15]
    print(sum_of_list(your_list))
