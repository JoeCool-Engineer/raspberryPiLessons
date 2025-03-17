x = float(input("Input a number for x: "))
y = float(input("Input a number for y: "))
z = x + y
w = z%2
print(x, " + ", y, " = ", z)
if  z>0 and w==0:
	print('Your answer is positive and even!')
elif z>0 and w!=0:
	print('Your answer is positive and odd!')
elif z<0 and w==0:
	print('Your answer is negative and even!')
elif z<0 and w!=0:
	print('Your answer is negative and odd!')
else:
	print('Your answer is zero!')
