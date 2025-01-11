list_asc = [1,2,3,6,9,14,20]
new_element1 = 13
new_element2 = 19

for i in range(len(list_asc)):
    if list_asc[i] > new_element2:
        list_asc.insert(i, new_element2)
        break
print(list_asc)