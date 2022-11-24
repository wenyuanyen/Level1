US_first_male = {'James', 'Robert', 'John', 'Michael', 'David',
                 'William', 'Richard', 'Joseph', 'Thomas', 'Charles',
                 'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Mark',
                 'Donald', 'Steven', 'Paul', 'Andrew', 'Joshua'}
UK_first_male = {'Oliver', 'George', 'Arthur', 'Noah', 'Muhammad',
                 'Leo', 'Oscar', 'Harry', 'Archie', 'Jack',
                 'Henry', 'Charlie', 'Freddie', 'Theodore', 'Thomas',
                 'Finley', 'Theo', 'Alfie', 'Jacob', 'William'}

# a. Find the first names that appear in both sets.
print(US_first_male.intersection(UK_first_male))
# b. Find the first names that appear in the United States set, but not Britain.
print(US_first_male.difference(UK_first_male))
# c. Find the first names that appear in the Britain set, but not United States.
print(UK_first_male.difference(US_first_male))
# d. Use a set comprehension to create a subset of names that have more than five letters.
USUK_first_male = US_first_male.union(UK_first_male)
print({name for name in USUK_first_male if len(name)>5})