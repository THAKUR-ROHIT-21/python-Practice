# it's Dictionary Comprehension.

def num(base,exp):
    if exp ==0:
        return 1
    return base * num(base,exp-1)
print(num(2,3))

# Using pow() Function method

base= 4
exp = 6
result= pow(base,exp)
print(f"power {result}" )