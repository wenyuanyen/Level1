from Exercise_1 import *


def verifyMortgages_Length(miniMortgages, standardMortgages, jumboMortgages, unfiltered):
    if len(miniMortgages) + len(standardMortgages) + len(jumboMortgages) == len(unfiltered):
        print('Validation Passed.')
    else:
        print(
            'Validation Failed: The number of mortgages for each sub-category do not add up to the total number mortgages.')


if __name__ == '__main__':
    mortgage_amounts = getMortgages(100)
    mini, std, jumbo = filterMortgages(mortgage_amounts)

    verifyMortgages_Length(mini,std,jumbo,mortgage_amounts)
