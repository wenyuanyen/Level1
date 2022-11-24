if __name__ == '__main__':
    names = ['Ari','Bob','Coco','David','Eva','Freda','Gary','Henry','Iris','Janice']
    ages = [16,19,17,23,21,22,15,24,18,19]
    print(list(zip(names,ages))) # zip is obj
    names_adult= [name for name, age in zip(names,ages) if age >= 18]
    print(names_adult)
