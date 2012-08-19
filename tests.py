from adder import calculate


def assert_calculation(expr, expected):
    result = calculate(expr)
    if  result != expected:
        print 'Error: {0!r} = {1}, not {2}.'.format(expr, result, expected)
        raise AssertionError


def test_number():
    assert_calculation('42', 42)


def test_addition():
    assert_calculation('1+1', 2)


def test_addition_2():
    assert_calculation('1+2', 3)


def test_add_with_spaces():
    assert_calculation('1 + 2', 3)


def test_subtraction():
    assert_calculation('10 - 3', 7)


def test_multiple_additions():
    assert_calculation('1 + 2 + 3', 6)


def test_mixed_operators():
    assert_calculation('10 * 2 + 3', 23)


def test_order_of_operations():
    assert_calculation('3 + 10 * 2', 23)


def test_order_of_operations_2():
    assert_calculation('10 - 3 * 2', 4)


if __name__ == '__main__':
    print '\nRunning tests:'
    passed_tests = total_tests = 0
    for key, value in locals().items():
        if key.startswith('test_'):
            total_tests += 1
            try:
                value()
                print '.',
                passed_tests += 1
            except AssertionError as e:
                print 'F', key

    print '\nPassed {0}/{1} tests.'.format(passed_tests, total_tests)
