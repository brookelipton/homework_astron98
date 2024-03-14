import numpy as np 
array = np.array([[1,1,1],[1,2,3,],[2,2,2]])
def findingequal(array):
    equal_rows = np.all(array[:, 1:] == array[:, :-1], axis = 1)
    return array[equal_rows]
print(findingequal(array))


array2 = np.zeros((8,8), dtype = int)
array2[1::2,::2] = 1
array2[::2,1::2] = 1
print(array2)


array3 = np.array(["coding", "is", "hard"])
result = np.char.join(" ", array3)
print(result)


np.random.seed(12345)
matrix = np.random.randint(1,50, (4,5))
def sorting(matrix):
    sorted_matrix = np.sort(matrix,axis = 0)
    return sorted_matrix
print(matrix)
sorted_matrix = sorting(matrix)
print(sorted_matrix)
