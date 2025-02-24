#   通过for循环和zip并行迭代来将两个列表中的元素相加

python_list1 = [1, 2, 3, 4]
python_list2 = [5, 6, 7, 8]

print( python_list1 + python_list2 )
# 结果为两个列表中的元素合并为一个列表，而不是将其中的元素相加

python_list3 = [(i1 + i2) for i1,i2 in zip(python_list1, python_list2)]
print(python_list3)

import numpy as np

numpy_array1 = np.array([1,2,3,4])
numpy_array2 = np.array([5,6,7,8])
print(numpy_array1 + numpy_array2)

list_long = list(range(1000000))
%timeit [(item * 2) for item in list_long]

%array_long = np.array(list_long)
%timeit array_long * 2