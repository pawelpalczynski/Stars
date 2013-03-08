from nodebox.graphics import *

class Sky(Layer):
	def __init__(self, *args, **kwargs):
		Layer.__init__(self, *args, **kwargs)
		self.stars = list()
		for i in range(50):
			self.stars.append([random() * canvas.width, random() * canvas.height])

	def draw(self):
		fill(1)
		stroke(1)
		for i in self.stars:
			star(i[0], i[1], points = 5, inner = 2, outer = 5)