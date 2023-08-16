#importing numpy and sympy
from sympy import *

#taking input for the size of the matrix
rows = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

#creating a temperoray list matrix
listMatrix = []

#loop that stores the values in the matrix
for i in range(rows):		 
	a =[]
	print("enter row {}".format(i+1))
	for j in range(col):	 
		a.append(int(input()))
	listMatrix.append(a)

#creating a sympy matrix object and printing it	
nonReducedMatrix = Matrix(listMatrix)
print(nonReducedMatrix)

#calculating the reduced form
reducedMatrix = nonReducedMatrix.rref()  

#printing the final answer with pivot columns
print("The Row echelon form of matrix M and the pivot columns : {}".format(reducedMatrix))  
