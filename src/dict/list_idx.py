

def list_idx(my_list):
    d = {}

    idx = 0
    for x in my_list:
        d[x] = idx
        idx += 1

    return d


if __name__ == "__main__":
    your_list = [chr(ord('a') + idx) for idx in range(26)]

    print(your_list)

    d = list_idx(your_list)

    print(d["a"])
    print(d["b"])
    print(d["e"])

