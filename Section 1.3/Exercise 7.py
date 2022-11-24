def person(name, age, **kwargs):
    print(name,age)
    print(kwargs.get('state'))
    print(kwargs.get('height'))
    print(kwargs.get('weight'))

if __name__ == '__main__':
    person('Jack', 27)
    person('Jack', 27, state='IL')
    person('Jack', 27, state='IL', height=172, weight=68, hairColor='Black')