import random
import string

# Extend the mortgage function to return a dict of address:mortgage.
def getMortgagesInfo_dict(numberOfMortgage):
    mortgageDict = dict()
    while len(mortgageDict) < numberOfMortgage:
        address = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        # tuple(amount in dollars, rate between 0%~10%, term in months with max 12 months)
        mortgageInfo = (random.randint(100000, 1000000), random.random() * 0.1, random.randint(1, 12))
        mortgageDict[address] = mortgageInfo

    return mortgageDict