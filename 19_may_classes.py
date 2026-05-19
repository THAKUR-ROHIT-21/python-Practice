# What is Function in python
# Every function has their own purpose.
# A function is a block of instraction which execute inside its own block
# Function is reusable means define one time use manytime (DRY :- Don't reprt  )
# Function has two main part first function defination secound function calling
# in python by Default return none value

# How to define function in python


def add(): # () parameter
    a=20
    b=30
    c=a+b
    print(c)
add() # () argunment

# Function into four category 
#1. Take nothing return nothing
#2. Take nothing return something
#3. Take something return nothing
#4. Take something return something

# Parameter (para) and argument (arg)

# positional parameter
def add(a,b):
    c=a+b
    print(c)
add(10,20)


# function

def table_print(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

table_print(int(input("Enter your Number :- ")))

function

def add(a=1,b=1):
    print(a+b)


def add1(a,b):
    print("Add=",a+b)


def add2(a,b):
    print("Sub =",a-b)


def add3(a,b):
    print("Mute=",a*b)


def add4(a,b):
    print("Div =",(a//b))

while True:
    num1=int(input("Enter your First number :- "))
    num2=int(input("Enter your  number :- "))
    opt=input("chose option : +, - , *, / (if you chose 0) :- ")
    if opt =="+":
        add1(num1,num2)
    elif opt=="-":
        add2(num1,num2)
    elif opt=="*":
        add3(num1,num2)
    elif opt=="/":
        add4(num1,num2)
    else :
        print("Wrong key")




# return

def ad(a,b):
    c=a+b
    return c
res=ad(2,3)
print(res)

def ad1(a,c):
    print(a+c)
ad1(10,res)

def greet(a):
    return a

def user_name(a):
    return a



print(greet("Hello"),user_name("Rohit"))



