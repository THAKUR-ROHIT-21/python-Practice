 # Waf to check number pass by argument ids odd and even

# def add(a):
#     if a%2==0:
#         print("Even Number")
#     else:
#         print("Odd Number")
# while True:
#     add(int(input("Enter your number :- ")))


# Waf a function to check which number is greater to number pass by user

# def add(a,b):
#     if a > b:
#         print("a is greater then b :-" ,a)
#     else:
#         print("b is greater then a :-",b)

# num1= int(input("Enter your a number :- "))
# num2=int(input("Enter your b number :- "))
# while True:
#     add(num1,num2)


# def chart(a):
#     if a in "aeiouAEIOU":
#         print("Vowel")
#     else:
#         print("Consonant")
# while True:
#     chart(input("Enter your character :- "))

# Waf to check is number completly divide by 2 and 3 and return 
# Yes number completly divide
# not devide

# def add(a):
#     if a%2==0 and a%3==0:
#         return f"Divided by 2 0r 3 :- {a}"
#     else:
#         return f"not divided by 2 or 3 :- {a}"
# num4=int(input("Enter your number :- "))
# res=add(num4)
# print(res)

# Waf to return lenth of a string pass by user len()

def add(a):
    c=0
    for i in a:
        c+=1
    return c

str1= input("Enter your String :- ") 
res= add(str1)
print(res)


