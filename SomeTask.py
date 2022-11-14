my_list=list(map(int, input('Enter space-separated integers: ').split()))
command=int(input("Command = "))
for i in  range(0,len(my_list)):
    if my_list[i] % 2 == 0 and command == 1:
        my_list[i] += 10
    if my_list[i] % 2 != 0 and command == 0:
        my_list[i] += 5
    print(my_list[i], end=" ")