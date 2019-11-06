
#python basics
#numpy for scientific computing
import numpy as np

#variables
x = 9
print(x)

# creating a list, a data-type in python
abc = [1.98,2.97,"gold",3.83,"silver",7.96,6.99]

print("The list values are as below")

#for loop in python
for x in abc:
    print (x)

#accessing list via index
print(abc[-1])

#calling a method
abc.append("copper")

print(abc)

#calling a function
print(len(abc))

#printing only part of the list
print(abc[1:3])

#saving an array in numpy which maintains a n dimensional object
a = np.array([2,9,10,67])

print(a)
