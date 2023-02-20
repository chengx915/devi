# lambda关键字用于创建小巧的匿名函数。`lambda a, b: a+b`
# 函数返回两个参数的和。Lambda 函数可用于任何需要函数对象的地方。
# 在语法上，匿名函数只能是单个表达式。在语义上，它只是常规函数定义的语法糖。
# 与嵌套函数定义一样，lambda 函数可以引用包含作用域中的变量

def make_incrementor(n):
    return lambda x: x + n


f = make_incrementor(3)
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
