from matplotlib import pyplot as plt
import numpy as np
import math
import time

#TODO:
#Create plot (Cartesian coordinates)
#Create plot (r-theta coordinates)
#Translate function to plot given domain


#INIT VAR SPACE: testing trig functions
x = np.arrange(0,4*np.pi,0.1) # start, stop, step
y = np.sin(x)

print("""Please select your coordinate system (type the corresponding 
		number):""")
print("\t1) Cartesian (x-y)")
print("\t2) Polar (r-θ)\n")
plot_system = int(input())

print("\n\nPlease enter a function:")
print("--------------QUICK GUIDE------------------")

print("""\nFor trigonometric functions, please use three-letter 
abbreviations (i.e., sin, cos, tan, csc, sec, cot)""")

print("""\nFor polynomials of order n >= 1, use a caret (^) to denote 
exponents and normal letters of the same case to denote variables""")
print("\te.g. y = x^2 + x + 1")

print("""\nFor square roots, use sqrt(x) in your input. For any other root,
use the corresponding exponent.""")

print("""\nFor rational functions, use paranthesis to help the program
distinguish between the numerator and denominator""")

print("\nFor Euler's number, use the letter e.")
print("""\nFor pi (π), you may either use π, pi, Pi.""")

print("\n-------------------------------------------\n")

f = input()

if plot_system == 1:
	print("graphing...")
	print(f.split())
	 
def create_cart_plot():
	"""Create a 2D Cartesian plot"""
	plt.subplot() 
	plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
	plt.xlabel("x")
	plt.ylabel("y")
	plt.grid()
	plt.show()

