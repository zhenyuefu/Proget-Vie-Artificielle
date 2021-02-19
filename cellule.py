from random import *

class Cellule:

	def __init__(self, x, y):

		self.x,self.y = x,y
		self.altitude = randint(0,100)

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getAltitude():
		return self.altitude
