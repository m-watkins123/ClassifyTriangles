import unittest
def classifyTriangles(A,B,C):
	print ("Input lenghts of the triangles sides")

A= input ("Enter side A")

B = input ("Enter side B")

C = input ("Enter side C")

if A == B == C:
	print("Equal Sides")
	pass
elif A == B or B == C or C == A:
	print("Isocles")
	pass
else:
	print ("Scalene")
	pass
