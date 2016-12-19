import functools


def perform(opr, a, b=None):
    """
    Calculating a logical expression
    """
    return {
        '!': lambda x, y: not x,
        '*': lambda x, y: x and y,
        '+': lambda x, y: x or y,
        '>': lambda x, y: (not x) or y,
        '=': lambda x, y: x == y
    }[opr](a, b)


def solve(expression):
    """
    Solve expression in postfix notation.
    """
    allowed_opr = ['!', '*', '+', '>', '=']
    stack = []

    for token in expression:
        if token in allowed_opr:
            b = stack.pop()
            a = stack.pop()
            res = perform(a, b, token)
            stack.append(res)
        else:
            stack.append(token)

    return stack.pop()
