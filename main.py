import pyglet
import random
from pyglet.gl import glClearColor
from pyglet.window import mouse

# Window Variables
WIDTH = 720
HEIGHT = 480
caption = "MineSweeper"

# Create Window & Batch
window = pyglet.window.Window(WIDTH, HEIGHT, caption=caption)
rectangle_batch = pyglet.graphics.Batch()
line_batch = pyglet.graphics.Batch()
# Change Background
glClearColor(128, 128, 128, 1.0)

buttons = []
# Sprites


class Rectangle:
    def __init__(self, x, y, has_bomb):
        self.has_bomb = has_bomb
        self.hidden = True

        self.sprite = pyglet.shapes.Rectangle(
            x, y, width=60, height=40, color=(128, 128, 128), batch=rectangle_batch)

    def on_click(self):
        self.hidden = False
        pass


buttons = []
lines = []


class Grid(Rectangle):
    def create_grid(*self):
        # Create Rectangles
        for height in range(0, 8*60, 40):
            for width in range(0, 12*60, 60):
                buttons.append(
                    Rectangle(width, height, random.choice([True, False]))
                )
        for i in range(0, WIDTH, 60):
            lines.append(pyglet.shapes.Line(i, 0, i, HEIGHT,
                         width=4, color=(0, 0, 0), batch=line_batch))
            for i in range(0, HEIGHT, 60):
                lines.append(pyglet.shapes.Line(0, i, WIDTH, i,
                             width=4, color=(0, 0, 0), batch=line_batch))


@window.event
def on_draw():
    window.clear()
    rectangle_batch.draw()
    line_batch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    pass


def update():
    pass


Grid.create_grid()


if __name__ == "__main__":
    pyglet.app.run()
