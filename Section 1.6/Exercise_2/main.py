from Mortgage_Dict.MortgageConstruct.Info.getMortgagesInfo import *
from Mortgage_Dict.MortgageSummary.Term.getMortgagesTerm import *
from Calculators.Maturity.Weighted_by_Loan.WeightedAverageMaturity import *
from Calculators.Rate.Weighted_by_Loan.WeightedAverageRate import *


def main():
    # Redo Exercise 1.5.8
    mortgageDict = getMortgagesInfo_dict(100)
    mortgageInfoList = sorted(mortgageDict.values(), key=lambda mortgageInfo: mortgageInfo[0], reverse=True)
    print(WeightedAverageRate(mortgageInfoList))
    print(WeightedAverageMaturity(mortgageInfoList))
    Term_dict = getMortgagesTerm_dict(mortgageDict)
    print(Term_dict)


if __name__ == "__main__":
    main()
