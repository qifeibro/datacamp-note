# Alternative to Python lists
# num_list = list(range(5))

import numpy as np
nums_np = np.array(range(5))
print(nums_np) # [0 1 2 3 4]

# NumPy array homogeneity
nums_np_ints = np.array([1, 2, 3])
print(nums_np_ints) # [1 2 3]
print(nums_np_ints.dtype) # int64

nums_np_floats = np.array([1, 2.5, 3])
print(nums_np_floats) # [1.  2.5 3. ]
print(nums_np_floats.dtype) # float64

# Python lists don't support broadcasting
nums = [-2, -1, 0, 1, 2]
# nums ** 2

# For loop (inefficient option)
sqrd_nums = []
for num in nums:
    sqrd_nums.append(num ** 2)
print(sqrd_nums) # [4, 1, 0, 1, 4]

# List comprehension (better option but not best)
sqrd_nums = [num ** 2 for num in nums]
print(sqrd_nums) # [4, 1, 0, 1, 4]

# NumPy array broadcasting
nums_np = np.array(nums)
print(nums_np ** 2) # [4 1 0 1 4]

# 2-D list
nums2 = [ [1, 2, 3],
          [4, 5, 6] ]

# 2-D array
nums2_np = np.array(nums2)

# Basic 2-D indexing (lists)
print(nums2[0][1]) # 2

# Basic 2-D indexing (arrays)
print(nums2_np[0, 1]) # 2

# to return the first column of values
print([row[0] for row in nums2]) # [1, 4]
print(nums2_np[:,0]) # [1 4]


# NumPy array boolean indexing
nums = [-2, -1, 0, 1, 2]
nums_np = np.array(nums)

# to gather only positive numbers
# create a boolean mask using a simple inequality
print(nums_np > 0) # [False False False  True  True]
print(nums_np[nums_np > 0]) # [1 2]

# No boolean indexing for lists
# For loop (inefficient option)
pos = []
for num in nums:
    if num > 0:
        pos.append(num)
print(pos) # [1, 2]

# List comprehension (better option but not best)
pos = [num for num in nums if num > 0]
print(pos) # [1, 2]
