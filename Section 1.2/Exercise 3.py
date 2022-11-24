if __name__ == '__main__':
    l = [i for i in range(1,1001) if i % 2 == 0]
    for i,num in enumerate(l):
        if i < len(l)-1:
            print(str(num)+',')
        else:
            print(str(num))