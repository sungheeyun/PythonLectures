def size(x, y, z):
    num_set = set()
    for i1 in range(3):
        for i2 in range(3):
            for i3 in range(3):
                num_set.add(abs(float(i1 - 1) * x - float(i2 - 1) * y + float(i3 - 1) * z))

    return len(num_set) - 1


def choose_comb():
    for x in range(1, 13):
        for y in range(x + 1, 13):
            z = 13 - x - y
            if z <= y:
                continue
            yield x, y, z


if __name__ == "__main__":
    for x, y, z in choose_comb():
        print(x, y, z, size(x, y, z))
