list = []
def input_integer():
    flag = False
    while not flag:
        try:
            n = int(input("Enter number: "))
            flag = True
        except ValueError:
            print("Please enter again: ")
    return n
length = int(input("Enter the length of list which you want to enter : "))
for i in range(length):
    n = input_integer()
    list.append(n)
print(list)
