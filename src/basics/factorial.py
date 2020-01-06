"""
This examples shows that how we can implement a function which evaluates the factorial of the number given
 as an argument and returns it.
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
        result = result * x

    return result


if __name__ == "__main__":
    m = 10
    print(m, "! =", factorial(m))
