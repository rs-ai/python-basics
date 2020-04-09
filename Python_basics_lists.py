# welcome to python basics

#variables
tutorialName ="python_basics"
print(tutorialName)

#using % operator
print("This section is  %s" %tutorialName)

#casting examples, you can cast, even change integer to strings etc
a = 100
b = 900.7865
print(float(a))
print (int(b))

print(" a and b original values are: "+str(a)+ " and "+str(b))

#lists - a collection
countries = ['USA','UK','Canada','Australia','New Zealand']
print(countries)

#navigating python indexes - they start at 0. We can traverse from the end starting at -1
print("The second one from first is "+countries[1]+ " second from last is " + countries[-2])

# You can change elements in a list by assigning the values you want against the index number.
# in this case i want to change the first two names to represent the full names
countries[0]= "United States of America"
countries[1] = "United Kingdom"
print (countries)

#slicing a list - there are ways you can only access a sub-section of a list
# this is referred to as slicing [:] - all ,[1:]- start with index 1, [2:4] - do 2 and 3, this excludes 4
# [:4] - start from 0 till 3, excluding 4
print(countries[2:4])
print(countries[3:])
#really cool - striding a list, 3 variables list[a:b:c] where a and b represent start and end
# while c represents the number by which we skip between indexes
# so countries[0:4:2] will skip one index value and will go to every second value
print(countries[0:4:2])

#removing items from the list using del, it can be applied againt a range as well
countries = countries + ["ASIA"]
print (countries[-1])
#oops .. mistake that's a continent, let's remove that from the list
del countries[-1]

