# 内置的 [`range()`]函数要求独立的 *start* 和 *stop* 实参。
# 如果这些参数不是独立的，则要在调用函数时，用 `*` 操作符把实参从列表或元组解包出来：

a = list(range(3, 6))
args = [3, 6]
c = list(range(*args))

print(a, c)

print("-" * 40)


# 同样，字典可以用 `**` 操作符传递关键字参数：
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

print("-" * 40)


# 例
def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))
