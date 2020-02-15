import math

EPS = 1e-07
DELTA = EPS / 2

SQRT_OF_5 = math.sqrt(5)
# Golden ratio coefficients
GR_COEFF_1 = (3 - SQRT_OF_5) / 2
GR_COEFF_2 = (SQRT_OF_5 - 1) / 2
# Fibonacci coefficients
FIB_COEFF_1 = (1 + SQRT_OF_5) / 2
FIB_COEFF_2 = (1 - SQRT_OF_5) / 2


def f(x):
    return (x - 2) ** 2


def dichotomy(a, b):
    return (a + b - DELTA) / 2, (a + b + DELTA) / 2


def golden_ratio(a, b):
    return a + GR_COEFF_1 * (b - a), a + GR_COEFF_2 * (b - a)


def fibonacci_number(n):
    return (FIB_COEFF_1 ** n - FIB_COEFF_2 ** n) / SQRT_OF_5


def fibonacci(a, b):
    n = 1
    while fibonacci_number(n + 2) <= (b - a) / EPS:
        n += 1

    return a + fibonacci_number(n) / fibonacci_number(n + 2) * (b - a), \
           a + fibonacci_number(n + 1) / fibonacci_number(n + 2) * (b - a)


def write_to_file(string='', mode='w', path='output.txt'):
    try:
        with open(path, mode) as fout:
            fout.write(string)
    except IOError:
        print('Error')


def search_of_min(a, b, func):
    # write_to_file(str(a) + '\n', 'a')
    # write_to_file(str(b) + '\n', 'a')
    # write_to_file(str(b - a) + '\n', 'a')

    if (b - a) < EPS:
        return (a + b) / 2

    x1, x2 = func(a, b)

    # write_to_file(str(x1) + '\n', 'a')
    # write_to_file(str(x2) + '\n', 'a')

    f1 = f(x1)
    f2 = f(x2)

    # write_to_file(str(f1) + '\n', 'a')
    # write_to_file(str(f2) + '\n', 'a')

    if f1 == f2:
        # write_to_file(str((x2-x1)/(b-a)) + '\n', 'a')
        return search_of_min(x1, x2, func)
    elif f1 < f2:
        # write_to_file(str((x2-a)/(b-a)) + '\n', 'a')
        return search_of_min(a, x2, func)
    else:
        # write_to_file(str((b-x1)/(b-a)) + '\n', 'a')
        return search_of_min(x1, b, func)


def min_interval_search(x0):
    x = [x0]
    f0 = f(x[0])
    h = DELTA

    if f0 > f(x[0] + DELTA):
        x.append(x0 + DELTA)
        h *= 1
    elif f0 > f(x[0] - DELTA):
        x.append(x0 - DELTA)
        h *= -1

    k = 1
    while True:
        h *= 2
        x.append(x[k] + h)
        
        if f(x[k]) > f(x[k + 1]):
            k += 1
        else:
            break

    return [x[k - 1], x[k + 1]]


def main():
    interval = (-2, 20)
    # write_to_file('Dichotomy\n')
    print('Dichotomy')
    res = search_of_min(interval[0], interval[1], dichotomy)
    print('Min of f(x) is located at', res)

    # write_to_file('\nGolden ratio\n', 'a')
    print('\nGolden ratio')
    res = search_of_min(interval[0], interval[1], golden_ratio)
    print('Min of f(x) is located at', res)

    # write_to_file('\nFibonacci\n', 'a')
    print('\nFibonacci')
    res = search_of_min(interval[0], interval[1], fibonacci)
    print('Min of f(x) is located at', res)

    print('\nMinimum interval search')
    res = min_interval_search(interval[0])
    print('Min of f(x) is located at', res)


if __name__ == '__main__':
    main()
