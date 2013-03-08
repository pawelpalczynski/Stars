from nodebox.graphics import *
import player, sky, planet

def setup(canvas):
	canvas.width = canvas.screen.width
	canvas.height = canvas.screen.height
	canvas.fullscreen = True

	canvas.append(sky.Sky(0, 0, name = sky))
	canvas.append(planet.Planet(mass = 50, size = 100, x = canvas.width/2, y = canvas.height/2, name = planet))
	canvas.append(player.Player(mass = 1, x = canvas.width/4, y = canvas.height/2, name = player))

def update(canvas):
	pass

def draw(canvas):
	canvas.clear()
	background(0)
	pass

def stop(canvas):
	pass

canvas.run(setup = setup, draw = draw, update = update, stop = stop)