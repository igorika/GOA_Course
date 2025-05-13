def math_position(x,position):
    # ! 2
    arr = []
    while x > 0:
        sum = x
        arr.append(sum)
        x = x // 2
        return arr[: : -1]
    print(math_position(5,8))