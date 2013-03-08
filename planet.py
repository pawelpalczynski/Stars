from entity import Entity
from nodebox.graphics import *

class Planet(Entity):
	def __init__(self, size, *args, **kwargs):
		Entity.__init__(self, *args, **kwargs)
		self.size = size
		self.width = size
		self.height = size

	def draw(self):
		ellipse(self.size/2, self.size/2, self.size, self.size)
		super(Planet, self).draw()