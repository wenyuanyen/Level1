from Exercise_1 import *


def MaxMinMortgages(miniMortgages, standardMortgages, jumboMortgages):
    maxmins = [min(miniMortgages), max(miniMortgages),
               min(standardMortgages), max(standardMortgages),
               min(jumboMortgages), max(jumboMortgages)]
    return maxmins


if __name__ == '__main__':
    mortgage_amounts = getMortgages(100)
    mini, std, jumbo = filterMortgages(mortgage_amounts)
    print(MaxMinMortgages(mini, std, jumbo))
