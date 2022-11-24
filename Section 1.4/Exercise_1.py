import random

# a. A function that returns an unsorted list of mortgage amounts, in thousands. Numbers
# should range from 100 to 1,000 and do not need to all be unique.

def getMortgages(numberOfMortgage):
    return [random.randint(100, 1000) for i in range(0, numberOfMortgage)]


# b. Filter the result of (a) into three lists: Amounts below 200, amounts between 200 and 467,
# and amounts greater than 467. Call these ‘miniMortgages’, ‘standardMortgages’, and
# ‘jumboMortgages’ respectively.

def filterMortgages(mortgages):
    if all([100 <= amount <= 1000 for amount in mortgages]):
        miniMortgages = [amount for amount in mortgages if amount < 200]
        standardMortgages = [amount for amount in mortgages if 200 <= amount <= 467]
        jumboMortgages = [amount for amount in mortgages if amount > 467]
        return sorted(miniMortgages), sorted(standardMortgages), sorted(jumboMortgages)
    else:
        print('Some mortgage loan has balance not in [100,1000],thousands.')


# c. Use the 'all' function with an if statement to verify that the resulting lists of b) indeed contain
# only numbers within the specified ranges.
def verifyMortgages_All(miniMortgages, standardMortgages, jumboMortgages):
    if all([z < 200 for z in miniMortgages]) and all([200 <= z <= 467 for z in standardMortgages]) and all(
            [z > 467 for z in jumboMortgages]):
        print('Validation Passed.')
    else:
        print('Validation Failed: Some mortgage put in wrong category.')


# d. Use the 'any' function with an if statement to verify that the resulting lists of b) indeed
# contain only numbers within the specified range
def verifyMortgages_Any(miniMortgages, standardMortgages, jumboMortgages):
    if not any([z >= 200 for z in miniMortgages]) and not any(
            [z < 200 or z > 467 for z in standardMortgages]) and not any([z <= 467 for z in jumboMortgages]):
        print('Validation Passed.')
    else:
        print('Validation Failed: Some mortgage put in wrong category.')


if __name__ == '__main__':
    mortgage_amounts = getMortgages(100)
    mini, std, jumbo = filterMortgages(mortgage_amounts)

    print('Mini Mortgages: 100 <= amount <200')
    print(mini)
    print('Standard Mortgages: 200 <= amount <=467')
    print(std)
    print('Jumbo Mortgages: 467 < amount <= 1000')
    print(jumbo)

    verifyMortgages_All(mini, std, jumbo)
    verifyMortgages_Any(mini, std, jumbo)
