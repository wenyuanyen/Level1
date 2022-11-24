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