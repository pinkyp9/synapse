import itertools
lst1 = ['0001','0011','0101','1011','1101','1111']
lst = [int(i,2) for i in lst1] 
print(f'the list is {lst}')
combinations = []
for r in range(1,len(lst)):
    for combination in itertools.combinations(lst, r):
        combinations.append(combination)
difference =[]
for items in combinations:
    res = [i for i in lst if i not in items]
    difference.append(abs(sum(res)-sum(items)))
print(f"the minimum difference is:{sorted(difference)[0]}")