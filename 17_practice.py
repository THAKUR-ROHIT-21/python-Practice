# 01.WAP to print 1 to 10 and Skip 3 and 6

num1=int(input("Enter Your First :- "))
num2=int(input("Enter Your Secound :- "))

while num1 <num2:
    num1+=1
    if num1==3 or num1==6:
        continue
    print(num1) 


# 02. For Exprience

i = 1
while i < 6:
  print(i)
  i += 2

# 03.Print a message once the condition is false.

i =0

while i<10:
    print(i)
    i+=1
else:
    print(" I is Longer then 10")


# 04.WAP to write fruit name and get a specific name to break using for loop

fruits= ["Apple","Banana","cherry"]

for i in fruits:
    print(i)
    if i=="Banana":
        break

# 05.WAP to write fruit name and get a specific name to break using while loop

fruits1= ["Apple","Banana","cherry"]

num1=0
while num1 < len(fruits1):
    print(fruits1[num1])
    if fruits1[num1]=="Banana":
        break
    num1+=1