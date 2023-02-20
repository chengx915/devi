# 列表推导式创建列表的方式更简洁。
# 常见的用法为，对序列或可迭代对象中的每个元素应用某种操作，用生成的结果创建新的列表；或用满足特定条件的元素创建子序列。
squares = []
for x in range(10):
    squares.append(x ** 2)

squares

squares = list(map(lambda x: x ** 3, range(10)))

squares = [x ** 4 for x in range(10)]
