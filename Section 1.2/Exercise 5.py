if __name__ == '__main__':
    l_even = [i for i in range(1, 1001) if i % 2 == 0]
    l_odd = [i for i in range(1, 1001) if i % 2 == 1]
    l_combined = l_even + l_odd
    # Create an aggregate list from 3) and 4) and print it out, separated by commas.
    for i,num in enumerate(l_combined):
        if i < len(l_combined)-1:
            print(str(num)+',')
        else:
            print(str(num))

    # Print out the aggregate list from 5), backwards and separated by commas.
    for i,num in enumerate(l_combined[::-1]):
        if i < len(l_combined)-1:
            print(str(num)+',')
        else:
            print(str(num))