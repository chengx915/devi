# 定义函数斐波拉契数列1
def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# 定义函数斐波拉契数列2
def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# 默认值只计算一次，下面的函数会累积后续调用时传递的参数
def f1(a, L=[]):
    L.append(a)
    return L


# 不想在后续调用之间共享默认值时，应以如下方式编写函数
def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# 调用函数
fib(100)
print(fib)

f = fib
f(100)
print(f)

print(fib2(100))
print(fib2)

print(f1(1))
print(f1(3))
print(f1(2))
