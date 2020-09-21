if __name__ == '__main__':
    x = 21
    y = 7

    while x != y:
        if x > y:
            x -= y
        else:
            y -= x

    print(x)
    print(y)