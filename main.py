import pyglet
from pyglet.gl import glClearColor

# Window Variables
WIDTH = 720
HEIGHT = 480
caption = "MineSweeper"

# Create Window & Batch
window = pyglet.window.Window(WIDTH, HEIGHT, caption=caption)
batch = pyglet.graphics.Batch()
# Change Background
glClearColor(128, 128, 128, 1.0)


@window.event
def on_draw():
    window.clear()
    batch.draw()


@window.event()
def on_mouse_press():
    pass


def update():
    pass


buttons = []
lines = []


def create_visual_grid():
    # Create Rectangles
    for height in range(0, 8*60, 40):
        for width in range(0, 12*60, 60):
            buttons.append(pyglet.shapes.Rectangle(
                width, height, width=60, height=40, color=(128, 128, 128), batch=batch))

    # Create Grid Lines, so player can tell which button is which
    for i in range(0, WIDTH, 60):
        lines.append(pyglet.shapes.Line(i, 0, i, HEIGHT,
                     width=4, color=(0, 0, 0), batch=batch))
    for i in range(0, HEIGHT, 60):
        lines.append(pyglet.shapes.Line(0, i, WIDTH, i,
                     width=4, color=(0, 0, 0), batch=batch))

    dimensions = [12, 8]
    return dimensions


# Setup for Game Loop
dimensions = create_visual_grid()


if __name__ == "__main__":
    pyglet.app.run()
