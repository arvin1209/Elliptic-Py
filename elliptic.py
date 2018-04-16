import numpy as np
import sympy as sp
O = np.nan
class Point:
	def __init__(self,*arg):
		self.O = np.nan
		if(arg[0] == self.O):
			self.inf = True
			self.x = None
			self.y = None
		if(len(arg)==2):
			self.x = x	
			self.y = y
			self.inf = False
	def add(self,point,curve):
		if(not (curve.haspoint(point) and curve.haspoint(self)))
		if(point.x == self.x and point.y == -self.y):
			return point(self.O)
		elif(point.x == self.x and point.y == self.y and point.y == 0):
			return point(self.O)
		else:
			equ = sp.sympify(str((curve.evaly(point.x)-curve.evaly(self.x))/(point.x-self.x))+"*x+"+str(curve.evaly())+"-y")
			ans = solveset(sp.Eq(equ,curve.equations),"x")
			for i in range(len(ans)):
				if ans[i] == point.x:
					ans.del(i)
				elif ans[i] == self.x:
					ans.del(i)
			return -ans[0]
class Elliptic:
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.O = np.nan
		self.determinant = -16(4*a**3+27b**2)
		self.equation()
		if(not self.issmooth()):
			raise Exception("Curve is not smooth")
	def evaly(self,x):
		return ((x**3+self.a*x+self.b),-(x**3+self.a*x+self.b))
	def issmooth(self):
		return self.determinant != 0
	def deriv(self,point):
		return (3*point.x**2+self.a)/(2*y)
	def equation(self):
		self.equations = sp.sympify("x**3-"+str(self.a)+"*x"+str(self.b)+"-y**2")
	def haspoint(self,point):
		if(point.inf):
			return True
		else:
			for i in evaly(point.x):
				if(i == point.y):
					return True
		return False
