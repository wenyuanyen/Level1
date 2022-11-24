from Exercise_1 import *


def SumMortgages(mortgages):
    return sum(mortgages)


if __name__ == '__main__':
    mortgage_amounts = getMortgages(100)
    print(SumMortgages(mortgage_amounts))
