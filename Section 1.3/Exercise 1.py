def weekdays(num):
    names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    numbers = [i for i in range(1,8)]
    if num not in numbers:
        return num, 'n.a.'
    else:
        return num, names[num-1]


if __name__ == '__main__':
    print(weekdays(1))
    print(weekdays(5))
    print(weekdays(7))
    print(weekdays(11))
    print(weekdays(-1))
    print(weekdays(0))

