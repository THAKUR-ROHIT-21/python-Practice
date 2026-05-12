# Traversing of string using range()

n1= "Rohit Kumar Thakur"
n=len(n1)

for i in range(n):
    print(n1[i],n1,i)


# Interview Question 

n2= "*"
r=""

for i in range(0,10):
    for j in range(0,i):
        print(n2,end=" ")
    print(" ")

# Reverce method without using (-,+)
n3= "THAKUR"
r_v= ""

for i in n3:
    r_v=i+r_v
print(r_v)

n4 = "THAKUR"

l= len(n4)

for i in range(l,1):
    print(n4[i], n4,i)
print(l)


# Using start and step

n4 = "THAKUR"
l= len(n4)
for i in range(0,l,2):
	print(n4[i], n4,i)




