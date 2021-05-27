import pyglet
from pyglet.gl import glClearColor
# Window Variables
WIDTH = 720
HEIGHT = 480
caption = "MineSweeper"

# Create Window
window = pyglet.window.Window(WIDTH, HEIGHT, caption=caption)
# Change Background
glClearColor(255, 255, 255, 1.0)


@window.event
def on_draw():
    window.clear()

@window.event()
def on_mouse_press():
    pass

def update():
    pass

if __name__ == "__main__":
    pyglet.app.run()