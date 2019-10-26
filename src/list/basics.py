

# variable name

# (alphabet or underbar) + (alphabet or underbar or digits)


if __name__ == "__main__":
    l = ['a', 2, 'c', 4, 5, 6]
    #    0    1   2   3  4  5
    # :2 -> 0, 1
    # 2:5 -> 2, 3, 4

    print('# basic indexing')

    print(l)
    print(l[0])
    print(l[1])
    print(l[2])
    print(l[3])

    print(l[:2])
    print(l[2:5])
    print(l[4:6])
    print(l[4:100])
