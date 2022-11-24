def person(name, age, **kwargs):
    print(name,age)
    for key, value in kwargs.items():
        print(key+':'+str(value))

if __name__ == '__main__':
    person('Jack', 27)
    person('Jack', 27, state='IL')
    person('Jack', 27, state='IL', height=172, weight=68, hairColor='Black')