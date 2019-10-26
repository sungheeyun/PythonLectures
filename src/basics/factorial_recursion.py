"""
Here we show that the factorial function can be implemented using recursion.
Note that the initial condition is critical.
"""


def factorial_recursion(n):
    """
    Return the factorial of n using recursion.

    Parameters
    ----------
    n :
        an integer of which the factorial is evaluated.

    Returns
    -------
    result :
        The factorial of n.
    """
    if n == 1:
        return 1

    return factorial_recursion(n - 1) * n


if __name__ == "__main__":
    m = 10
    print(m, '! =', factorial_recursion(m))
