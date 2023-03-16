""" Turtles Circling Simple Model - Chapter 0 """

import math
import random
import tkinter as tk

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
NUM_TURTLES = 40
TURTLE_RADIUS = 5
TURTLE_SPEED = 5

class Turtle:

    def __init__(self, canvas, x, y, angle):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0.35
        self.shape = canvas.create_oval(x-TURTLE_RADIUS, y-TURTLE_RADIUS,
                                         x+TURTLE_RADIUS, y+TURTLE_RADIUS,
                                         fill="black")
   

    def move(self):
        dx = self.speed*math.cos(math.radians(self.angle))
        dy = self.speed*math.sin(math.radians(self.angle))
        self.x += dx
        self.y += dy
        if self.x < 0 or self.x > CANVAS_WIDTH or self.y < 0 or self.y > CANVAS_HEIGHT:
            # Wrap around the edges of the canvas
            self.x %= CANVAS_WIDTH
            self.y %= CANVAS_HEIGHT
        if self.canvas is not None and self.canvas.itemcget(self.shape, "state") != "hidden":
            self.canvas.move(self.shape, dx, dy)
            self.angle -= 1
            self.canvas.itemconfig(self.shape, tags=f"turtle angle_{self.angle}")

    
    def update_angle(self, angle):
        self.angle = angle
        self.canvas.itemconfig(self.shape, tags=f"turtle angle_{self.angle}")


def create_gui():
    global canvas, turtles
    root = tk.Tk()
    root.title("Turtles Circling")
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.grid(row=0, column=0, sticky="nsew")
    button_frame = tk.Frame(root)
    button_frame.grid(row=1, column=0, sticky="nsew")
    setup_button = tk.Button(button_frame, text="Setup", command=setup_circle)
    setup_button.pack(side="left")
    run_button = tk.Button(button_frame, text="Run Model", command=run_model)
    run_button.pack(side="left")
    quit_button = tk.Button(button_frame, text="Quit", command=root.destroy)
    quit_button.pack(side="left")
    root.mainloop()

def setup_circle():
    global turtles
    if "turtles" in globals():
        for turtle in turtles:
            canvas.delete(turtle.shape)
    turtles = []
    angle_step = 360/NUM_TURTLES
    for i in range(NUM_TURTLES):
        angle = i*angle_step
        x = CANVAS_WIDTH/2 + math.cos(math.radians(angle))*CANVAS_WIDTH/4
        y = CANVAS_HEIGHT/2 + math.sin(math.radians(angle))*CANVAS_HEIGHT/4
        turtle = Turtle(canvas, x, y, angle)
        turtles.append(turtle)


def move_turtles():
    global turtles
    for turtle in turtles:
        turtle.move()
    if canvas is not None and canvas.winfo_exists():
        canvas.after(50, move_turtles)
    else:
        turtles = []

def run_model():
    global turtles
    setup_circle()
    while True:
        move_turtles()
        canvas.update()

create_gui()
