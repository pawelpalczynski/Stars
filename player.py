from nodebox.graphics import *
import math

from entity import Entity

class Player(Entity):
	def __init__(self, *args, **kwargs):
		Entity.__init__(self, *args, **kwargs)
		self.clr = Color(0.5, 0.5, 0.5, 0.5)
		self.image = Image(path = "res/player.png")
		self.width = self.image.width
		self.height = self.image.height

		self.acceleration_power = 500
		self.rotation_power = 3

	def draw(self):
		image(self.image)
		super(Player, self).draw()

		# fill(1, 0, 0)
		# stroke(1, 0, 0)
		# orientation = self.ori*50
		# orientation.rotate(-self.rotation)
		# orientation.draw(self.width*self.relative_origin[0], self.height*self.relative_origin[1])

		# fill(0, 1, 0)
		# stroke(0, 1, 0)
		# velocity = self.vel*1
		# velocity.rotate(-self.rotation)
		# velocity.draw(self.width*self.relative_origin[0], self.height*self.relative_origin[1])

		# fill(0, 0, 1)
		# stroke(0, 0, 1)
		# acceleration = self.acc*1
		# acceleration.rotate(-self.rotation)
		# acceleration.draw(self.width*self.relative_origin[0], self.height*self.relative_origin[1])

	def update(self):
		super(Player, self).update()
		for k in canvas.keys:
			if k == 'd':
				self.rotate(-self.rotation_power)
				self.ori.rotate(-self.rotation_power)
			elif k == 'a':
				self.rotate(self.rotation_power)
				self.ori.rotate(self.rotation_power)
			if k == 'w':
				self.forces.append(self.ori * self.acceleration_power) 
			elif k == 's':
				self.forces.append(-self.ori * self.acceleration_power) 