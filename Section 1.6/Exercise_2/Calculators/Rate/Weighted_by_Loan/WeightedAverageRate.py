def WeightedAverageRate(mortgageInfoList):
    WAR = 0.0
    total_face_amount = 0.0
    # each tup has (amount,rate,term)
    for amount, rate, term in mortgageInfoList:
        WAR += amount * rate
        total_face_amount += amount
    WAR = WAR / total_face_amount
    return round(WAR * 100, 2)