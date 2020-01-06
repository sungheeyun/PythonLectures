def is_palindrome_1(string):
    for idx in range(int(len(string) / 2)):
        if string[idx] != string[-idx - 1]:
            return False
    return True


def is_palindrome_2(string):
    return string == string[::-1]
