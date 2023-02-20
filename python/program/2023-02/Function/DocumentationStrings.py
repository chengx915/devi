# 文档字符串
# 第一行应为对象用途的简短摘要。为保持简洁，不要在这里显式说明对象名或类型，
# 因为可通过其他方式获取这些信息（除非该名称碰巧是描述函数操作的动词）。
# 这一行应以大写字母开头，以句点结尾。
#
# 文档字符串为多行时，第二行应为空白行，在视觉上将摘要与其余描述分开。
# 后面的行可包含若干段落，描述对象的调用约定、副作用等。
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)
