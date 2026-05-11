# it's Dictionary Comprehension.

# def num(base,exp):
#     if exp ==0:
#         return 1
#     return base * num(base,exp-1)
# print(num(2,3))

# Using pow() Function method
# in power function base **exp it means : 4**6 :- 4x4x4x4x4x4=4096
# base= 4
# exp = 6
# result= pow(base,exp)
# print(f"power {result}")

# Logic method in python

for i in range(1,10):
    for j in range(0,i):
        print("*",end=" ")
    print(" ")