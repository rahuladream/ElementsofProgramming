import itertools
numbers = [4,3,2,5,6,7,2,5,5]
result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == 9]
print (result)