import turtle
from tkinter import Tk, Label, Button, filedialog, messagebox
from PIL import Image

def convert_image_to_turtle_code():
    filename = filedialog.askopenfilename(initialdir="/", title="Select an Image",
                                          filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")))
    image = Image.open(filename).convert("RGB")

    screen = turtle.Screen()
    screen_width = image.width
    screen_height = image.height
    screen.setup(screen_width, screen_height)
    screen.tracer(0)

    turtle_obj = turtle.Turtle()
    turtle_obj.speed(0)
    prev_color = None
    turtle_code = ""

    try:
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = image.getpixel((x, y))
                turtle_x = x - (image.width // 2)
                turtle_y = (image.height // 2) - y

                turtle_obj.penup()
                turtle_obj.goto(turtle_x, turtle_y)
                turtle_obj.pendown()

                current_color = (r, g, b)
                if current_color != prev_color:
                    turtle_obj.pencolor(r / 255, g / 255, b / 255)
                    turtle_code += f"turtle.pencolor({r / 255}, {g / 255}, {b / 255})\n"
                    turtle_obj.dot()
                    turtle_code += "turtle.dot()\n"
                    prev_color = current_color

        turtle_obj.hideturtle()
        screen.update()

    except turtle.Terminator:
        pass

    messagebox.showinfo("Turtle Code", f"Image converted to turtle code successfully!\n\nTurtle Code:\n\n{turtle_code}")

root = Tk()
root.title("Image to Turtle Code Converter")

label = Label(root, text="Click the button to convert an image to Turtle code and paint it using turtle.")
label.pack()

button = Button(root, text="Select Image", command=convert_image_to_turtle_code)
button.pack()

root.mainloop()

