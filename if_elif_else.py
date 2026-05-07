#use of if, elif and else

str = input("Enter traffic light color :-")

if str == "Red" :
	print("Wait for green light")
elif str == "Yellow" :
	print("Ready for go")
elif str == "Green" :
	print("Go for your destination")
else :
	print("traffic Color is not match")

print("_"*100)

cl1= "Red"
cl2= "Green"
cl3= "Yellow"
color= input("Enter your Favorate Color :- ")

if color ==cl1:
	print("Yes Red color is in the box")
elif color == cl2:
	print("Yes Green color is in the box")
elif color == cl3:
	print("Yes Yellow color is in the box")
else:
	print("This color is not in the box")