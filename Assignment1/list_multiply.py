# def multiplyList(myList) : 
      
#     # Multiply elements one by one 
#     result = 1
#     for x in myList: 
#          result = result * x  
#     return result  
      
# # Driver code 
# list1 = [1, 2, 3]  
# list2 = [3, 2, 4] 
# print(multiplyList(list2)) 

# ussing numpy library

# Python3 program to multiply all values in the 
# list using numpy.prod() 
  
import numpy  
list1 = [1, 2, 3]  
list2 = [3, 2, 4] 
  
# using numpy.prod() to get the multiplications  
result1 = numpy.prod(list1) 
result2 = numpy.prod(list2) 
print(result1) 
print(result2) 