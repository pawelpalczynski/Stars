from nodebox.graphics import *

class Entity(Layer):
	def __init__(self, mass, *args, **kwargs):
		Layer.__init__(self, *args, **kwargs)
		self.pos = physics.Vector(self.x, self.y, 0)
		self.ori = physics.Vector(1, 0, 0)
		self.vel = physics.Vector(0, 0, 0)
		self.acc = physics.Vector(0, 0, 0)

		self.relative_origin = 0.5, 0.5

		self.friction = 0.5
		self.mass = mass
		self.forces = list()

	def update(self):
		# Physics
		force_sum = physics.Vector()
		for f in self.forces:
			force_sum += f
		self.acc = force_sum/self.mass

		delta = canvas.elapsed
		self.vel += (self.acc - self.vel * self.friction)*delta
		self.pos += self.vel*delta

		self.forces = list()

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

	def addForce(self, force):
		self.forces.append(force)

	def draw(self):
		fill(1, 0, 0)
		stroke(1, 0, 0)
		orientation = self.ori*50
		orientation.rotate(-self.rotation)
		orientation.draw(self.width*self.relative_origin[0], self.height*self.relative_origin[1])

		fill(0, 1, 0)
		stroke(0, 1, 0)
		velocity = self.vel*1
		velocity.rotate(-self.rotation)
		velocity.draw(self.width*self.relative_origin[0], self.height*self.relative_origin[1])

		fill(0, 0, 1)
		stroke(0, 0, 1)
		acceleration = self.acc*1
		acceleration.rotate(-self.rotation)
		acceleration.draw(self.width*self.relative_origin[0], self.height*self.relative_origin[1])