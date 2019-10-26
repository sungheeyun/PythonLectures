
def m_table(n):
    """
    Prints a multiplication table for n.

    Parameters
    ----------
    n :
        Integer for which multiplication table is printed.
    """
    print('>>', n)
    for x in range(2, 10):
        print('\t', n, 'x', x, '=', n * x)


def table_9_9():
    """
    Print all 9 multiplication tables.
    """
    for n in range(2, 10):
        m_table(n)


if __name__ == "__main__":
    table_9_9()
