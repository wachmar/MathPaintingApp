from canvas import Canvas
from shapes import Square, Rectangle

# Welcome
print("Hey user, lets play a drawing game")
print("First we need a canvas")

# Get the canvas width and height
canvas_width = int(input("Enter canvas width:"))
canvas_height = int(input("Enter canvas height:"))

# Get the canvas color
colors = {"white" : (255,255,255), "black": (0,0,0)}
canvas_color = input("Enter canvas color (white or black)")

# Create the canvas
canvas = Canvas(width=20, height=30, color=colors[canvas_color])

# Draw stuff onto the canvas
keep_adding_shapes = 1

while keep_adding_shapes:
    shape_type = input("What would you like to draw (rectangle or square), type \"quit\" to stop.")

    if shape_type.lower() == "rectangle":
        r_x = int(input(f"Enter x of the {shape_type}"))
        r_y = int(input(f"Enter y of the {shape_type}"))
        r_width = int(input(f"Enter width of the {shape_type}"))
        r_height = int(input(f"Enter height of the {shape_type}"))
        red = int(input(f"How much red should the {shape_type} have? (0 - 255)"))
        green = int(input(f"How much green should the {shape_type} have? (0 - 255)"))
        blue = int(input(f"How much blue should the {shape_type} have? (0 - 255)"))
        #Draw it
        r1 = Rectangle(x=r_x, y=r_y, width=r_width, height=r_height, color=(red, green, blue))
        r1.draw(canvas)

    elif shape_type.lower() == "square":
        s_x = int(input(f"Enter x of the {shape_type}"))
        s_y = int(input(f"Enter y of the {shape_type}"))
        s_side = int(input(f"Enter side of the {shape_type}"))
        red = int(input(f"How much red should the {shape_type} have? (0 - 255)"))
        green = int(input(f"How much green should the {shape_type} have? (0 - 255)"))
        blue = int(input(f"How much blue should the {shape_type} have? (0 - 255)"))
        # Draw it
        s1 = Square(x=s_x, y=s_y, side=s_side, color=(red, green, blue))
        s1.draw(canvas)

    elif shape_type.lower() == "quit":
        keep_adding_shapes = 0
        break

# Create the image
canvas.make("canvas.png")