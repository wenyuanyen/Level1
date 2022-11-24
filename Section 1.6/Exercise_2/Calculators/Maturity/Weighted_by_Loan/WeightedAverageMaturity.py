def WeightedAverageMaturity(mortgageInfoList):
    WAM = 0.0
    total_face_amount = 0.0
    # each tup has (amount,rate,term)
    for amount, rate, term in mortgageInfoList:
        WAM += amount * term
        total_face_amount += amount
    WAM = WAM / total_face_amount
    return WAM