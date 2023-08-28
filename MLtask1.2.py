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
new_lst_index = difference.index(min(difference))
lst1 = list(combinations[new_lst_index])
lst2 = [i for i in lst if i not in lst1]
lst4= lst1+lst2
while(len(lst2)!=1):
    sum = lst2[0]+lst2[1]
    lst2.pop(1)
    lst2.pop(0)
    lst2.append(sum)
    lst4 =lst2+lst1
    print(sorted(lst4))
while(len(lst1)!=1):
    sum = lst1[0]+lst1[1]
    lst1.pop(1)
    lst1.pop(0)
    lst1.append(sum)
    lst4 = lst2+lst1
    print(sorted(lst4))
print(f"the minimum difference is:{abs(lst4[1]-lst4[0])}")