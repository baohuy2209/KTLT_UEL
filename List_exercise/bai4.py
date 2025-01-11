list_1 = [1,2,7,10,20,23,31]
list_2 = [3,5,9,11,13,17]
list_result = []
i = j = 0
while i < len(list_1) and j < len(list_2):
    if list_1[i] < list_2[j]:
        list_result.append(list_1[i])
        i+= 1
    else:
        list_result.append(list_2[j])
        j += 1
while i < len(list_1):
    list_result.append(list_1[i])
    i += 1
while j < len(list_2):
    list_result.append(list_2[j])
    j += 1
print(list_result)