mortgage_term = {10, 15, 30}

# a. Add a 5-year term to the set.
mortgage_term.add(5)
print(mortgage_term)
# b. Remove the 15-year term from the set.
mortgage_term.remove(15)
print(mortgage_term)
# c. Remove a 45-year term from the set. What happens? [using .remove() caused errors]How can you prevent that? [use .discard()]
mortgage_term.discard(45)
print(mortgage_term)
