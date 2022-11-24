import random
import string


# Extend the mortgage function to return a dict of address:mortgage.
def getMortgages_dict(numberOfMortgage):
    mortgageDict = dict()
    while len(mortgageDict) < numberOfMortgage:
        address = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        mortgage = random.randint(100, 1000)
        mortgageDict[address] = mortgage

    return mortgageDict


def filterMortgages_dict(mortgagesDict):
    miniMortgages = {address: mortgage for address, mortgage in mortgagesDict.items() if mortgage < 200}
    standardMortgages = {address: mortgage for address, mortgage in mortgagesDict.items() if 200 <= mortgage <= 467}
    jumboMortgages = {address: mortgage for address, mortgage in mortgagesDict.items() if mortgage > 467}
    return miniMortgages, standardMortgages, jumboMortgages


if __name__ == '__main__':
    # dict of address:mortgage
    random.seed(2022)
    mortgageDict = getMortgages_dict(10)

    # a. Provide three separate dicts, filtered the same way as problem 1).
    miniDict, stdDict, jumboDict = filterMortgages_dict(mortgageDict)
    print('All Mortgages')
    print(mortgageDict)
    print('Mini Mortgages: 100 <= amount <200')
    print(miniDict)
    print('Standard Mortgages: 200 <= amount <=467')
    print(stdDict)
    print('Jumbo Mortgages: 467 < amount <= 1000')
    print(jumboDict)

    # b. Modify one value in the jumboMortgages dict. Check the original dict; did it remain
    # intact or change? Ans: Remain intact
    # Why? Because jumbo is a dictionary constructed separately
    print(jumboDict['TPLC29'])
    jumboDict['TPLC29'] = 500
    print(jumboDict['TPLC29'])
    print(mortgageDict['TPLC29'])

    # c. Extract the lists of amounts from each separate dict. Modify one value in the
    # miniMortgages list. Does the miniMortgages dict change? How about the original dict? Ans: Both unchanged
    # Why? Because the lists are created with values extracted from dict, and not referenced to original dictionary nor other list.

    mini_amt, std_amt, jumbo_amt = list(miniDict.values()), list(stdDict.values()), list(jumboDict.values())
    print(mini_amt[0])
    mini_amt[0] = 150
    print(mini_amt[0])
    print(miniDict)
    print(mortgageDict)

