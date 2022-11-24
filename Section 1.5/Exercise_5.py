countryPop = {'China': 1412600000, 'US': 332726406, 'Japan': 125502000, 'UK': 67081234, 'Germany': 83222442,
              'Switzerland': 8736500, 'France': 67853000, 'Netherlands': 17729981, 'Canada': 38713423,
              'Sweden': 10468482}
while True:
    userCountry = input('Enter the name of a country, or enter 0 to exit.')
    if userCountry == '0':
        break
    else:
        # If the country does not exist in the dict:
        if not countryPop.get(str(userCountry)):
            userCountryPop = input('The population is unknown. Enter the population of the country.')
            countryPop[str(userCountry)] = userCountryPop # Update the dict
        else:
            print('The country has population ' + str(countryPop.get(str(userCountry))))

# Display the final sorted dict
countryPop = dict(sorted(countryPop.items()))
for key, value in countryPop.items():
    print(str(key) + ' has population ' + str(value))

# sub-dictionary with countries of population greater than 1 billion.
countryPop_1bn = {country:pop for country,pop in countryPop.items() if pop > 10**9}
print(countryPop_1bn)