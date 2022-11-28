n = int(input("N - "))
dict={}
list=[]
for i in range(1,n*2+1):
    if i % 2 != 0:
       key=input("Key - ")
       dict[key]=None
    else:
        dict[key]=input("Value - ")
m = int(input("M - "))
for i in range(m):
    listValue = input(f"List value{i+1} - ")
    if dict.keys().__contains__(listValue):
        list.append(dict[listValue])
        continue
    list.append(listValue)

print(dict)
print(list)
