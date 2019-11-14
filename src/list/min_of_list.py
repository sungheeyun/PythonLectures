
def min_of_list(my_list):
    res = my_list[0]

    for element in my_list:
        if element < res:
            res = element
    return res


if __name__ == "__main__":

    your_list = [1, 3, 10, 15]
    print(min_of_list(your_list))

