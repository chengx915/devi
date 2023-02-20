# # 走向python编程第一步
# a, b = 0, 1
# while a < 1000:
#     print(a, end=',')
#     a, b = b, a + b

# # if语句
# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# match


def what_is(number):
    match number:
        case 1:
            print("one", number)
        case 2:
            print("two", number)
        case 3:
            print("three", number)
        case 4:
            print("four", number)
        case _:
            print("other!", number)


what_is(2)
