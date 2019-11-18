
def is_empty_2(my_list):
    return len(my_list) == 0


def is_empty_1(my_list):
    if my_list:
        return False
    else:
        return True


def is_empty(my_list):
    if len(my_list) == 0:
        return True
    else:
        return False


if __name__ == "__main__":

    your_list = [1, 2]
    your_list = []

    if is_empty_1(your_list):
        print(your_list, 'is empty!')
    else:
        print(your_list, 'is NOT empty!')
