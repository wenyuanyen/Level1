if __name__ == '__main__':
    x = [1, 2, 3, 4.5, 5, 6, 7.455, 8, 9, 10.9]
    # a. Display the first two numbers from the list (using indexing).
    print(x[:2])
    # b. Display the last two numbers.
    print(x[-2:])
    # c. Display all the numbers besides the last number, using a single print statement.
    print(x[:-1])
    # d. Display all the numbers besides the first number, using a single print statement.
    print(x[1:])
    # e. Display all the numbers besides the first two and last three numbers, using a single print.
    print(x[2:-3])
    # f. Append one number to the end of the list.
    x.append(11)
    print(x)
    # g. Append five numbers to the end of the list, using a single operation.
    x.extend([12,13.8,14,15,16])
    print(x)
    # h. Insert one number right after the third number in the list.
    x.insert(3,3.5)
    print(x)
    # i. Modify the fourth-to-last number in the list.
    x[3:] = [30.5, 40.5, 50, 60, 70.455, 80, 90, 100.9, 110, 120, 130.8, 140, 150, 160]
    print(x)
    # j. Display the list backwards, using splicing.
    print(x[::-1])
    # k. Display every second item in the list.
    print(x[1::2])
    # l. Display every second item in the list, backwards.
    print(x[-2::-2])
