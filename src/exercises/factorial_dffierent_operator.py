"""
Below we show that the statement

    result = result * x

can be rewritten to

    result *= x

Like this, Python provides operators such as

    +=
    -=
    *=
    /=
"""


def factorial(n):
    """
    Return the factorial of n.

    Parameters
    ----------
    n :
        an integer of which the factorial is evaluated.

    Returns
    -------
    result :
        The factorial of n.
    """
    result = 1
    for x in range(2, n + 1):
        result *= x

    return result


if __name__ == "__main__":
    m = 10
    print(m, '! =', factorial(m))
