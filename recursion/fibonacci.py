from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci_recursion(n):
    """Get fibonacci number recursively"""
    if n < 2:
        return n
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def fibonacci_iterator(n):
    """Get fibonacci number by iterator"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_generator(n):
    """Get fibonacci number by generator"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    import time

    x = 1000

    # print('='*80)
    # print(f'Print fibonacci numbers from 0 to {x}')
    # print('-' * 80)
    #
    # timer = time.perf_counter()
    # print(f'function: {fibonacci_recursion.__name__}(), "{fibonacci_recursion.__doc__}"')
    # for i in range(x):
    #     print(i, fibonacci_recursion(i))
    # print(round((time.perf_counter() - timer) * 1000, 2), 'ms')
    # print('-' * 80)
    #
    # timer = time.perf_counter()
    # print(f'function: {fibonacci_iterator.__name__}(), "{fibonacci_iterator.__doc__}"')
    # for i in range(x):
    #     print(i, fibonacci_recursion(i))
    # print(round((time.perf_counter() - timer) * 1000, 2), 'ms')
    # print('-' * 80)
    #
    # timer = time.perf_counter()
    # print(f'function: {fibonacci_generator.__name__}(), "{fibonacci_generator.__doc__}"')
    # for i, n in enumerate(fibonacci_generator(x)):
    #     print(i, n)
    # print(round((time.perf_counter() - timer) * 1000, 2), 'ms')
    # print('-' * 80)

    print('=' * 80)
    print(f'Print a list of fibonacci numbers from 0 to {x}')
    print('-' * 80)

    timer = time.perf_counter()
    print(f'function: {fibonacci_recursion.__name__}(), "{fibonacci_recursion.__doc__}"')
    print([fibonacci_recursion(f) for f in range(x)])
    print(f'{(time.perf_counter() - timer) * 1000 :.2f} ms')
    print('-' * 80)

    timer = time.perf_counter()
    print(f'function: {fibonacci_iterator.__name__}(), "{fibonacci_iterator.__doc__}"')
    print([fibonacci_iterator(f) for f in range(x)])
    print(f'{(time.perf_counter() - timer) * 1000 :.2f} ms')
    print('-' * 80)

    timer = time.perf_counter()
    print(f'function: {fibonacci_generator.__name__}(), "{fibonacci_generator.__doc__}"')
    print([f for f in fibonacci_generator(x)])
    # print(list(fibonacci_generator(x)))
    print(f'{(time.perf_counter() - timer) * 1000 :.2f} ms')
    print('-' * 80)
