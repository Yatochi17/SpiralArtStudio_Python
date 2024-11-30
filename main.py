import turtle
import random
from tkinter import *
from tkinter import ttk, colorchooser

class SpiralArtStudio:
    def __init__(self):
        # Initialize the main window
        self.root = Tk()
        self.root.title("Spiral Art Studio")

        # Create canvas for turtle
        self.canvas = Canvas(self.root, width=800, height=600)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Initialize turtle
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor('black')
        self.artist = turtle.RawTurtle(self.screen)
        self.artist.speed(0)  # Fastest speed
        self.artist.hideturtle()

        # Control panel
        self.control_panel = ttk.Frame(self.root, padding="10")
        self.control_panel.pack(side=RIGHT, fill=Y)

        # Color controls
        ttk.Label(self.control_panel, text="Pattern Controls").pack()

        # Color picker button
        self.color = '#ff0000'  # Default color
        ttk.Button(self.control_panel, text="Choose Color",
                  command=self.pick_color).pack(pady=5)

        # Size control
        ttk.Label(self.control_panel, text="Size:").pack()
        self.size_var = DoubleVar(value=50)
        self.size_slider = ttk.Scale(self.control_panel, from_=10, to=100,
                                   variable=self.size_var, orient=HORIZONTAL)
        self.size_slider.pack(fill=X, pady=5)

        # Rotation control
        ttk.Label(self.control_panel, text="Rotation:").pack()
        self.rotation_var = DoubleVar(value=45)
        self.rotation_slider = ttk.Scale(self.control_panel, from_=0, to=180,
                                       variable=self.rotation_var, orient=HORIZONTAL)
        self.rotation_slider.pack(fill=X, pady=5)

        # Pattern selector
        ttk.Label(self.control_panel, text="Pattern:").pack()
        self.pattern_var = StringVar(value="spiral")
        patterns = ttk.Combobox(self.control_panel, textvariable=self.pattern_var)
        patterns['values'] = ('spiral', 'star', 'flower', 'fractal')
        patterns.pack(pady=5)

        # Buttons
        ttk.Button(self.control_panel, text="Draw",
                  command=self.draw_pattern).pack(pady=5)
        ttk.Button(self.control_panel, text="Clear",
                  command=self.clear_canvas).pack(pady=5)

    def pick_color(self):
        color = colorchooser.askcolor(color=self.color)[1]
        if color:
            self.color = color

    def clear_canvas(self):
        self.artist.clear()
        self.screen.bgcolor('black')

    def draw_spiral(self):
        # Get parameters from sliders
        max_size = self.size_var.get()
        angle = self.rotation_var.get()
        self.artist.pencolor(self.color)

        # Start from center
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()

        # Calculate number of steps based on size and angle
        steps = int(360 / (angle if angle else 1))  # Prevent division by zero
        steps = min(max(steps * 5, 50), 200)  # Keep steps between 50 and 200

        # Calculate growth per step
        growth = max_size / steps

        # Draw spiral
        size = growth
        for _ in range(steps):
            self.artist.forward(size)
            self.artist.right(angle)
            size += growth

    def draw_star(self):
        size = self.size_var.get() * 2
        points = int(self.rotation_var.get() / 20)  # Convert rotation to points
        self.artist.pencolor(self.color)

        for _ in range(points):
            self.artist.forward(size)
            self.artist.right(180 - (180 / points))

    def draw_flower(self):
        size = self.size_var.get()
        petals = int(self.rotation_var.get() / 10)
        self.artist.pencolor(self.color)

        for _ in range(petals):
            self.artist.circle(size, 60)
            self.artist.left(120)
            self.artist.circle(size, 60)
            self.artist.left(180 - (180 / petals))

    def draw_fractal(self, length=None, depth=4):
        if length is None:
            length = self.size_var.get() * 2
            self.artist.pencolor(self.color)

        if depth == 0:
            self.artist.forward(length)
            return

        length = length / 3
        self.draw_fractal(length, depth-1)
        self.artist.left(60)
        self.draw_fractal(length, depth-1)
        self.artist.right(120)
        self.draw_fractal(length, depth-1)
        self.artist.left(60)
        self.draw_fractal(length, depth-1)

    def draw_pattern(self):
        self.artist.penup()
        self.artist.goto(0, 0)
        self.artist.pendown()

        pattern = self.pattern_var.get()
        if pattern == 'spiral':
            self.draw_spiral()
        elif pattern == 'star':
            self.draw_star()
        elif pattern == 'flower':
            self.draw_flower()
        elif pattern == 'fractal':
            self.draw_fractal()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    studio = SpiralArtStudio()
    studio.run()