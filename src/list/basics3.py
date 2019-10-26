
if __name__ == "__main__":

    my_list = []

    print(my_list)
    print(id(my_list))

    my_list.append(1)  # my_list <DOT> append
    print(my_list)
    print(id(my_list))

    my_list.append(2)
    print(my_list)
    print(id(my_list))

    my_list.append('beth')
    print(my_list)
    print(id(my_list))

    ####
    n = 10000

    # my_list = []
    my_list = list()

    for number in range(n):
        my_list.append(number)

    print(my_list)
    print(len(my_list))
    ####

    print(id(my_list))
