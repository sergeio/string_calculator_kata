from operator import add, sub, mul, div


def calculate(expr):
    """Evaluates the expression.

    Negative numbers are considered to be lame, and are thus not supported.

    """
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    order = reversed(['*', '/', '+', '-'])

    for op in order:
        if op in expr:
            numbers = map(calculate, expr.split(op, 1))
            return operators[op](numbers[0], numbers[1])

    return int(expr)
