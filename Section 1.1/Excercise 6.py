if __name__ == '__main__':
    print('Triangle Area Calculator\n')

    while True:
        base, height = input('Please input base and height, separated by a blank (enter 0 0 to exit)').split()
        base, height = float(base), float(height)

        if base == 0.0 and height == 0.0:
            break

        if base > 0.0 and height > 0.0:
            area = base * height / 2
            print('The area of the triangle is ' + str(area))
        else:
            print('Please input valid base/height of a triangle')

