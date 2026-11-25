# numpy 1d array slicing
import numpy as np
marks = np.array([10, 20, 30, 40, 50])
print(marks)
print("dimension:", marks.ndim)
print(marks[0:1])
print(marks[0:2])

# print 1st three elements, first any
print(marks[:2])

# print from particular element to end...
print(marks[2:])