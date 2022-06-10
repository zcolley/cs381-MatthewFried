import numpy as np
import pandas as pd
'''
1.
Write a Python/NumPy code block that finds the distinct/unique common items between these two
arrays:
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
Your output should contain only the distinct overlapping values. For example, if a 2 is found in both array a and array b,
your output should contain only one 2 even if array a contains more than one 2 within it.
'''
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
# print(list(set(a) & set(b)))

'''
2.
Create the following 5x3 array using knowledge you have of Python’s / NumPy’s sequencing functionality
so that you do not need to explicitly key in every integer value.
'''
arr_list = np.arange(1, 16)
new_shape_list = arr_list.reshape(3, 5).T
# print(new_shape_list)

'''
3.
The process of transforming a multidimensional array into a unidimensional array is referred to as “flattening”. Transform the 5x3 array shown above in Problem 2 into a unidimensional array such that the sequence of values contained within the array is as follows: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
'''
# print(new_shape_list.flatten('F'))

'''
4.ransform the 2-D array shown in Problem 2 into a 3 dimensional array such that the first column becomes the first dimension of the 3-D array, the second column becomes the second dimension of the 3-D array, and the third column becomes the third dimension of the 3-D array.
'''

three_d_array = np.reshape(new_shape_list, new_shape_list.shape+(1,))
# print(three_d_array)

'''
5. Transform the 3-D array you created in Problem 4 back to the 2-dimensional format shown in Problem 2.
'''
two_d_array = np.reshape(three_d_array, (5, 3))
# print(two_d_array)

'''
6.You are given the following two arrays:
a = np.array([12, 5, 7, 15, 3, 1, 8])
b = np.array([14, 6, 3, 11, 19, 12, 5])
Write a Python/Numpy code block that removes from array a any items that are also present in array b.

'''
a = np.array([12, 5, 7, 15, 3, 1, 8])
b = np.array([14, 6, 3, 11, 19, 12, 5])
a = set(a)
res = [val for val in b if val not in a]
print(res)
'''
7.What is the maximum yearly NYC consumption of water in millions of gallons per day?
How many calendar years are represented within this data set? NumPy's shape command is one way to find
out.
What is the mean and the standard deviation of the per capita daily water consumption?
What is the increase or decrease in population from year to year? Use NumPy's `diff` function to create an array
of differences and save that to a variable called "pop_diff", then print that variable to the screen.
'''
df = pd.read_csv(
    'https://raw.githubusercontent.com/zcolley/cs381-MatthewFried/main/hw/Module6_Data.csv')

df.columns = ['years', 'population', 'gallon', 'capita']
# print(df)
# 7(1)
print(df['gallon'].max())

# 7(2)
print(len(df['years']))

# 7(3)
print(df['capita'].mean())
print(df['capita'].max() - df['capita'].min())

# 7(4)
print(np.diff(df['years']))
