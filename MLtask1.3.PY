def explode_chain(lst):  
    for elements in lst:
        i = 0
        while(i+2<len(elements)):
            
            if((elements[i]+1 == elements[i+1]) and (elements[i]+2==elements[i+2])):
                del elements[i:i+3]
            else:
                i = i+1   
    return lst



encoded_list = [
    [1,2,3,4,6], 
    [5,7,8,9,15],
    [12,14,16,18],
    [10,11,12,13,16,17,18,20]
]

result  = explode_chain(encoded_list)
print(result)

