import numpy as np

from my_package.string_utils import shout

nums = [1,2,3,4,5]
arr = np.array(nums)
# print("Array:",arr)
# print("Mean:",np.mean(arr))

# print(np.sum(arr))
# print(np.max(nums))
# print(np.std(nums))
# print(np.square(nums))

matrix = np.array([nums,nums])
# print(matrix)
print(matrix.shape)
print(matrix.T)



