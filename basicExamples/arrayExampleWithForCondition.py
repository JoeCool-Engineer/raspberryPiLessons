myGrades = int(input('How many grades: '))
x  = []
mySum = 0
for i in range(0, myGrades, 1):
	myGrade = int(input('Input your grades: '))
	x.append(myGrade)

for i in range(0, myGrades, 1):
	mySum = x[i] + mySum
	print(f'My sum is {mySum} for grade {i}')
	myAvg = mySum/myGrades

print('My average grade: ', str(round(myAvg,2)))
print('Your grades are: ')

for i in range(0, myGrades, 1):
	print(x[i])

