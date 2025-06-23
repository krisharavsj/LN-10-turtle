def addition (p,q):
    return p+q
def subtraction(p,q):
    return p-q
def multiplication(p,q):
    return p*q
def division (p,q):
    return p/q
print("select any function")
print("a.add")
print("b.sub")
print("c.mult")
print("d.div")
choice=input("please enter your choice a,b,c,d")
numb_1=int(input("please enter the first number"))
numb_2=int(input("please enter your second number"))
if choice=='a':
    print(numb_1,"+",numb_2,"=",addition(numb_1,numb_2))
elif choice=='b':
    print(numb_1,"-",numb_2,"=",subtraction(numb_1,numb_2))
elif choice=='c':
    print(numb_1,"*",numb_2,"=",multiplication(numb_1,numb_2))
elif choice=='d':
    print(numb_1,"/",numb_2,"=",division(numb_1,numb_2))
else:
    print("THIS IS AN INVALID INPUT!!")