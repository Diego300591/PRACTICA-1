class Circulo():
	_radio=0
	def __init__(self,rad):
		self._radio=rad
	def darArea(self):
		Area=3.1416*(self._radio**2)
		return Area
radio=raw_input()
radio=float(radio)
calculo=Circulo(radio)
print calculo.darArea()
