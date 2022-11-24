def argsMean(*args):
    if all(isinstance(x, (int, float)) for x in args) and args:
        return sum(args) / len(args)


if __name__ == '__main__':
    print(argsMean(1, 2, 3))
    print(argsMean(1, 2, 3, 4, 5, 6))
    print(argsMean(1))
    print(argsMean())
    print(argsMean(1, '2', 3, 4, 5, 6))
    print(argsMean(*[1, 2, 3], *[4, 5, 6]))
    print(argsMean(*[1, 2, 3], *(4, 5, 6)))
    print(argsMean(*[1, '2', 3], *(4, 5, 6)))
