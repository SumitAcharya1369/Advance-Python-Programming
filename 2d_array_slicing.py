# numpy 2d array slicing
import numpy as np
marks = np.array([[10,20,30],
                  [30,40,50],
                  [60,70,80]])
print(marks)
print("dimension:", marks.ndim)

# print(marks[row start:row stop, col start:col stop])
print(marks[0:1,0:2])

# printing specific rows but all columns
print(marks[0:1,:])

# printing all rows but specific columns
print(marks[:,0:2])