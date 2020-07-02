def add():
    """
    无参数有返回值的函数
    :return:
    """
    a = int(input("请输入一个整数："))
    b = int(input("请输入另一个整数："))
    return a+b


def subtract(a, b):
    """
    有参数无返回值的函数，默认返回值为None
    :param a:
    :param b:
    :return:
    """
    print((a - b))


def multiply(a, b=0):
    """
    有参数有返回值的函数
    :param a:
    :param b:
    :return:
    """
    return a*b


