# # Python3 code to demonstrate
# # conversion of lists to dictionary
# # using dictionary comprehension
#
# # initializing lists
# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]
#
# # Printing original keys-value lists
# print ("Original key list is : " + str(test_keys))
# print ("Original value list is : " + str(test_values))
#
# # using dictionary comprehension
# # to convert lists to dictionary
# res = {test_keys[i]: test_values[i] for i in range(len(test_keys))}
#
# # Printing resultant dictionary
# print ("Resultant dictionary is : " +  str(res))
# ###^^
###vvhttps://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list
from collections import defaultdict

def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return ((key,locs) for key,locs in tally.items()
                            if len(locs)>1)


source = "ABABDBAAEDSBQEWBAFLSAFB"
for dup in sorted(list_duplicates(source)):
    print(dup)
###^^
