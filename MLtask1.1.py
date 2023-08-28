jumbled_superheroes = ["DocToR_sTRAngE","sPidERmaN","MoON_KnigHT","caPTAIN_aMERIca","hULK"] 
indices = []
decoded_names =  []

for index,value in enumerate(jumbled_superheroes):
    indices.append(index)
    value = value.replace("_"," ").lower()
    decoded_names.append(value)

f1 = lambda x:len(x)
name_lengths = list(map(f1,decoded_names))

temp = list(zip(indices,name_lengths))

f2 = lambda y:y[1]
sorted_names = sorted(temp,key=f2)
print(sorted_names)

c = 1
for i in sorted_names:
    print(f"{c}. {str.title(decoded_names[i[0]])}")
    c += 1
