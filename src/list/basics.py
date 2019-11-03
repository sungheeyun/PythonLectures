
# variable name
# (alphabet or underscore) + (alphabet or underscore or digits)

if __name__ == "__main__":
    my_list = ['a', 2, 'c', 4, 'beth_list', 6]

    print('# basic indexing')

    print(my_list)
    print(my_list[0])
    print(my_list[1])
    print(my_list[2])
    print(my_list[3])
    # print(aaaa[100])

    print(my_list[:2])
    print(my_list[2:5])
    print(my_list[4:6])

    print(my_list[3:])
    print(my_list[3:100])
