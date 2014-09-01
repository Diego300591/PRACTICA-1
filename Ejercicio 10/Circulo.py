class Circulo():
	_radio=0
	_Area=0
	def __init__(self,rad):
		self._radio=rad
		self.darArea()
	def darArea(self):
		self._Area=3.1416*self._radio**2
	def getArea(self):
		return self._Area
radio=raw_input()
radio=float(radio)
calculo=Circulo(radio)
print calculo.getArea()
