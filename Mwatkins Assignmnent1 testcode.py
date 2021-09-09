Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import unittest
>>> def classifyTriangles(A,B,C):
	print ("Input lenghts of the triangles sides")

	
>>> A = input ("Enter side A")
Enter side A 3
>>> B = input ("Enter side B")
Enter side B 4
>>> C = input ("Enter side C")
Enter side C 3
>>> if A == B == C:
	print("Equal Sides")
	pass
elif A == B or B == C or C == A:
	print("Isocles")
	pass
else:
	print ("Scalene")
	pass
quit()
SyntaxError: invalid syntax
>>> sys.exit()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    sys.exit()
NameError: name 'sys' is not defined
>>> 
= RESTART: C:/Users/manas/OneDrive/Email attachments/Pictures/Documents/Stevens Instuite of Technology Classes/Software Testing, Quality Assurance and Main/ClassifyTriangles.py
Enter side A 4
Enter side B 5
Enter side C 6
Scalene
>>> 