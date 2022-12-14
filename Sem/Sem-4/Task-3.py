def list_avg(lst,multiplier=1):
    avrg=0
    count=0
    for i in lst:
        if type(i)==int or type(i)==float:
           avrg += i * multiplier
           count+=1
        elif type(i)==str and i.isnumeric():
            avrg += int(i) * multiplier
            count += 1
    if count==0:
        return "Error: Division by zero\nNone"
    return avrg/count

print(list_avg(['4', 1.5, "@7$", 3.5, (1, "hi")]))

print(list_avg(['6', 3, 3.0], 2))

print(list_avg(['%$', {}]))

print(list_avg([]))
