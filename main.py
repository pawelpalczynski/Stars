from nodebox.graphics import *
import player

def setup(canvas):
	canvas.width = 1024
	canvas.height = 768
	canvas.x = (canvas.screen.width - canvas.width)/2
	canvas.y = (canvas.screen.height - canvas.height)/2

	canvas.fps = 60

	canvas.append(player.Player(canvas.width/2, canvas.height/2))

def update(canvas):
	pass

def draw(canvas):
	canvas.clear()
	background(0)

def stop(canvas):
	pass

canvas.run(setup = setup, draw = draw, update = update, stop = stop)