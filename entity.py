from nodebox.graphics import *

class Entity(Layer):
	def __init__(self, *args, **kwargs):
		Layer.__init__(self, *args, **kwargs)
		self.pos = physics.Vector(self.x, self.y, 0)
		self.ori = physics.Vector(1, 0, 0)
		self.vel = physics.Vector(0, 0, 0)
		self.acc = physics.Vector(0, 0, 0)

		self.relative_origin = 0.5, 0.5

		self.friction = 0.5

	def update(self):
		# Physics
		delta = canvas.elapsed
		self.vel += (self.acc - self.vel * self.friction)*delta
		self.pos += self.vel*delta

		# Boundary conditions
		if self.pos.x > canvas.width:
			self.pos.x = 0
		elif self.pos.x < 0:
			self.pos.x = canvas.width
		elif self.pos.y > canvas.height:
			self.pos.y = 0
		elif self.pos.y < 0:
			self.pos.y = canvas.height

		self.x = self.pos.x
		self.y = self.pos.y