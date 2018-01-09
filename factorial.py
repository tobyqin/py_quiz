"""
实现正整数阶乘函数。
5! = 5 * 4 * 3 * 2 * 1 = 120
"""


def factorial(n):
    if not isinstance(n, int):
         return None

    if n < 0:
        raise ValueError('n should be non-negative integer!')

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(20))