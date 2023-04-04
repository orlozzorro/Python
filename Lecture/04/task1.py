# def f(x):
#     return x*x

# a = f
# # print(type(f))
# # print(f(5))

# def calk1(a, b):
#     return a+b


def calk2(a, b):
    return a*b


def math(op, x, y):
    print(op(x, y))


calk1 = lambda a,b: a+b


math(lambda a,b: a+b, 5, 45)
