def multiply(x=2, greet = 'Your Answer'): 
    #default argument set to 2, if no argument is passed
    return (greet +' '+ str(x*2))

y = multiply()
print(y)
z = multiply(9.82)
print(z)


def setplurals(s):
    s=s+'s'
    return s
print(setplurals('cat'))
