def power(base,exp):
    if(expression==1):
        return(base)
    if(exp!=1):
        return(base*power(base,expression-1))
base=int(input("Enter base: "))
expression=int(input("Enter exponential value: "))
print("Result:",power(base,expression))
