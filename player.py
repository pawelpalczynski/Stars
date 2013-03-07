from nodebox.graphics import *

from entity import Entity

class Player(Entity):
	def __init__(self, *args, **kwargs):
		Entity.__init__(self, *args, **kwargs)
		self.clr = Color(0.5, 0.5, 0.5, 0.5)
		self.image = Image(path = "res/player.png")
		self.width = self.image.width
		self.height = self.image.height

		self.acceleration_power = 100
		self.rotation_power = 3

	def draw(self):
		rect(0, 0, self.width, self.height, fill = self.clr, stroke = Color(1))
		image(self.image)

		fill(1)
		stroke(1)
		self.pos.draw(-self.x + self.width*self.relative_origin[0], -self.y + self.height*self.relative_origin[1])

		fill(1, 0, 0)
		stroke(1, 0, 0)
		orientation = self.ori*50
		orientation.draw(self.width*self.relative_origin[0], self.height*self.relative_origin[1])

		fill(0, 1, 0)
		stroke(0, 1, 0)
		self.vel.draw(self.width*self.relative_origin[0], self.height*self.relative_origin[1])

		fill(0, 0, 1)
		stroke(0, 0, 1)
		self.acc.draw(self.width*self.relative_origin[0], self.height*self.relative_origin[1])


	def update(self):
		super(Player, self).update()
		self.acc = physics.Vector(0, 0, 0)
		for k in canvas.keys:
			if k == 'd':
			 	self.ori.in2D.rotate(-self.rotation_power)
			elif k == 'a':
			 	self.ori.in2D.rotate(self.rotation_power)

			if k == 'w':
				self.acc = self.ori * self.acceleration_power
			elif k == 's':
				self.acc = -self.ori * self.acceleration_power

	def on_mouse_enter(self, mouse):
		mouse.cursor = HAND

	def on_mouse_leave(self, mouse):
		mouse.cursor = DEFAULT