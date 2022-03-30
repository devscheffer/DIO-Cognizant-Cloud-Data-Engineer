import itertools

test = itertools.permutations('abc',3)
for idx,i in enumerate(test):
    print(idx,i)
