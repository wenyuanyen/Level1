import time

if __name__ == '__main__':
    # 0 to 10,000,000
    list_1 = [i for i in range(0, 10 ** 7 + 1)]

    # 0 to 10,000,000 that ends with 0
    start = time.time()
    list_2 = []
    for num in list_1:
        if num % 10 == 0:
            list_2.append(num)
    end = time.time()
    print('Loop elapsed time (sec): ' + str(end - start))

    # 0 to 10,000,000 that ends with 0
    start = time.time()
    list_3 = [i for i in list_1 if i % 10 == 0]
    end = time.time()
    print('List Comprehension elapsed time (sec): ' + str(end - start))

    # List comprehension is faster than for-loop because
    # the former doesn't need to load the append attribute of the list and call it as a function.
