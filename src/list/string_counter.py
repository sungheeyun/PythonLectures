
def string_counter(my_list):
    counter = 0
    for string in my_list:
        if len(string) > 1 and string[0] == string[-1]:
            counter += 1

    return counter


if __name__ == "__main__":
    sample_list = ['abc', 'xyz', 'aba', '1221', 'A', 'b']

    print(string_counter(sample_list))
