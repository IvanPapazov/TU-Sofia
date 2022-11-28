
def input_nums(n):
    list = []
    if type(n)==int or (type(n)==str and n.__str__().isnumeric()):
        for i in range(int(n)):
            num =input("N - ")
            if type(num)==int or (type(num)==str and num.__str__().isnumeric()):
                list.append(int(num))
    return list

def sum_list(lst):
    sum = 0
    for i in lst:
        if type(i)==int or type(i)==float:
            sum += i
        elif type(i) == str and i.isnumeric():
            sum += float(i)
    return sum

def max_of_two(a, b):
    if (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float) and a > b:
        return a
    elif (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float) and a < b:
        return b
    elif (type(a)==int or type(a)==float) and (type(b)==int or type(b)==float) and a == b:
        return a
    elif (type(a)==int or type(a)==float) and (type(b)!=int or type(b)!=float):
        return a
    elif (type(b)==int or type(b)==float) and (type(a)!=int or type(a)!=float):
        return b
    else:
        return

print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))
