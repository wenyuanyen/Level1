if __name__ == '__main__':
    list_1 = [i**2 for i in range(0, 101)]
    list_2 = [i**2 for i in range(0, 101) if i**2 > 1000]
    list_3 = [i**2 for i in range(0, 101) if i**2 > 1000 and i**2 % 2 == 0]

    print(list_1)
    print(list_2)
    print(list_3)