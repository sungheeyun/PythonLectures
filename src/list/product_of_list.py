def product_of_list(my_list):
    res = 1

    for element in my_list:
        res *= element

    return res


if __name__ == "__main__":

    your_list = [1, 3, 10, 15]
    print(product_of_list(your_list))
    print(product_of_list(range(1, 101)))
