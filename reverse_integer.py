def reverse(x:int) -> int:
    """
    :type x: int
    :rtype: int
    """
    up_limit = (1 << 31) - 1
    """
    up_limit = (1 << 31) - 1
    down_limit = -(1 << 31)
    if (x > up_limit):
        return 0

    if (x < down_limit):
        return 0
    """

    if (x >= -9 and x <= 9):
        return x

    nagetive = 0
    if (x < 0):
        nagetive = 1
        x = 0 - x

    i = 0
    output = 0
    tmp_output = 0
    while (True):
        tmp_output = x % 10

        if (output == 0 and tmp_output == 0):
            pass
        else:
            output = output * 10 + tmp_output

        x = x // 10
        if (x == 0):
            break

    if (output > up_limit):
        return 0

    if (nagetive == 1):
        return (0 - output)

    return output

print(reverse(901000))
