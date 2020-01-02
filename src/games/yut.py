from random import choice


BT_char_list = [("T", "B") if idx else ("T", "BB") for idx in range(4)]


def throw_yuts():
    bit_list = [choice((0, 0, 0, 0, 0, 1)) for idx in range(4)]
    print(" ".join([BT_char_list[idx][bit] for idx, bit in enumerate(bit_list)]))
    return (sum(bit_list) - 1) % 5 + 1


if __name__ == "__main__":
    print(throw_yuts())

