my_list = [1,3,28,11,10,19,29,30,21,23,26]
length = 1
count = 0
for i in range(1,len(my_list)):
    if my_list[i-1] < my_list[i]:
        length += 1
    else:
        count += (length*(length+1))/2
        length = 1
count += (length*(length+1))/2
print(count)