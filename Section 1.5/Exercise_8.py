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


def WeightedAverageRate(mortgageInfoList):
    WAR = 0.0
    total_face_amount = 0.0
    # each tup has (amount,rate,term)
    for amount, rate, term in mortgageInfoList:
        WAR += amount * rate
        total_face_amount += amount
    WAR = WAR / total_face_amount
    return round(WAR * 100, 2)


def WeightedAverageMaturity(mortgageInfoList):
    WAM = 0.0
    total_face_amount = 0.0
    # each tup has (amount,rate,term)
    for amount, rate, term in mortgageInfoList:
        WAM += amount * term
        total_face_amount += amount
    WAM = WAM / total_face_amount
    return WAM


def getMortgagesTerm_dict(mortgageDict):
    mortgageInfoList = mortgageDict.values() # list of tuple (amount,rate,term)
    TermDict = dict()
    for amount, rate, term in mortgageInfoList:
        if not TermDict.get(term):
            TermDict[term] = list()
            TermDict[term].append((amount, rate))
        else:
            TermDict[term].append((amount, rate))
    return dict(sorted(TermDict.items())) # dict sorted by term (key)



if __name__ == '__main__':
    # dict of address:mortgage
    random.seed(2022)
    mortgageDict = getMortgagesInfo_dict(100)
    print(mortgageDict)

    # a. Extract a list of tuple values from the dict, and sort the list by amount (descending).
    mortgageInfoList = sorted(mortgageDict.values(), key=lambda mortgageInfo: mortgageInfo[0], reverse=True)

    # b. Create a function that calculates the Weighted Average Rate of the mortgage pool. The
    # input parameter should be a list of mortgage tuples (amount,rate,term). Print the rate
    # percentage, rounded to the nearest hundredths.
    print(WeightedAverageRate(mortgageInfoList))

    # c. Create a function that calculates the Weighted Average Maturity (term) of the mortgage
    # pool. The input parameter should be a list of mortgage tuples (amount,rate,term).
    print(WeightedAverageMaturity(mortgageInfoList))

    # d. Create a new dict (by processing the original dict) with Term as the key and a list of
    # (amount, rate) tuples for each Term key.
    Term_dict = getMortgagesTerm_dict(mortgageDict)
    print(Term_dict)
