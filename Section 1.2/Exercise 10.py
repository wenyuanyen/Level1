if __name__ == '__main__':
    nestedList = [[1,22.0,'A'],['DE',5],[True,17,8,9.9]]
    flattenList = [item for sublist in nestedList for item in sublist]
    print(nestedList)
    print(flattenList)
