numbers_list = [num for num in range(51)]
print(numbers_list)
squared_list = [x ** 2 for x in numbers_list]
print(squared_list)


listA = [num for num in range(1,11)]
listB = [num for num in range (20,31)]
combo_listAB = listA + listB
odd_numbers = [num for num in combo_listAB if num % 2 !=0]
print(odd_numbers)


_2DList = []
#experienced syntax error here when I tried to name list 2D_list
for i in range(5):
    row = []
    for j in range(5):
        value = i * 5 + j + 1
        #replacing multiples of 3 here 
        if value % 3 == 0:
            row.append('?')
        else:
            row.append(value)
    _2DList.append(row)
for row in _2DList:
    print(row)
#experienced error (unexpected output) here when I called to print _2DList rather than row, fixed using print statements (3.1)
#experienced error (type error) in line 22, fixed using print statement
    

def remove_duplicates(list1):
    list2 = []
    for item in list1:
        if item not in list2:
            list2.append(item)
#experienced an error when running code and used the pritn statement to realize "items" was written in line 35 instead of "item"
    return list2
original_list = [1,2,3,4,5,6,6,7,8,8,9]
result = remove_duplicates(original_list)
print(result)
#I definitely needed help on this question, did not know where to start