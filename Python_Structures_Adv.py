#Tuples - immutable, you cannot change their values, notice the enclosure syntax
car_companies = ('Fiat','Mercedes-Benz','Vauxhall','Volkswagen')
print(car_companies)
#try deleting a value - you will get an error message

#del (car_companies[0])



# a dictionary is a structure that helps you hold and access key value pairs, curly brackets
# for enclosure, semi-colon : to seperate key and value
companies = {'name':'Microsoft', 'revenue':19000000000,'globalcompany':'True'}
print (companies['name'])
#you can call a dictionary directly using functions like dictionary.values(), dictionary.items() etc
print(companies.keys())
print(companies.values())
#print(companies.items())

#adding value to a dictionary
companies['city'] = 'Redmond'
#removing values from a dictionary using del function
del companies['globalcompany']
print(companies.items())