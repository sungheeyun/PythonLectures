class a(object):
    def __enter__(self):
        print("sss")
        return "sss111"

    def __exit__(self, type, value, traceback):
        print("ok")
        return False


if __name__ == "__main__":

    with a() as s:
        print(s)
