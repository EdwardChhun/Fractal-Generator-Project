import tkinter as tk
from PIL import Image, ImageDraw

# Mandelbrot parameters
WIDTH, HEIGHT = 800, 800
MAX_ITER = 1000
RE_START, RE_END = -2, 2
IM_START, IM_END = -2, 2

def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1
    return n

def generate_mandelbrot():
    img = Image.new('RGB', (WIDTH, HEIGHT), 'black')
    draw = ImageDraw.Draw(img)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            re = RE_START + (x / WIDTH) * (RE_END - RE_START)
            im = IM_START + (y / HEIGHT) * (IM_END - IM_START)
            c = complex(re, im)
            color = mandelbrot(c) 

            if color == 256:
                draw.point((x, y), (255, 255, 255))  # White for boundary points
            elif color < 256:
                draw.point((x, y), (0, 0, 255))  # Blue for points inside the Mandelbrot set
            else:
                draw.point((x, y), (0, 0, 0))  # Black for points outside the Mandelbrot set
            
    img.save('mandelbrot.png')
    img.show()
    img.save('mandelbrot.png')
    img.show()

def set_parameters():
    global WIDTH, HEIGHT, MAX_ITER, RE_START, RE_END, IM_START, IM_END
    WIDTH = int(width_entry.get())
    HEIGHT = int(height_entry.get())
    MAX_ITER = int(max_iter_entry.get())
    RE_START = float(re_start_entry.get())
    RE_END = float(re_end_entry.get())
    IM_START = float(im_start_entry.get())
    IM_END = float(im_end_entry.get())

root = tk.Tk()
root.title("Mandelbrot Fractal Generator")

# Create GUI menu for changing parameters
width_label = tk.Label(root, text="Width:")
width_label.pack()
width_entry = tk.Entry(root)
width_entry.pack()

height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

max_iter_label = tk.Label(root, text="Max Iterations:")
max_iter_label.pack()
max_iter_entry = tk.Entry(root)
max_iter_entry.pack()

re_start_label = tk.Label(root, text="Real Start:")
re_start_label.pack()
re_start_entry = tk.Entry(root)
re_start_entry.pack()

re_end_label = tk.Label(root, text="Real End:")
re_end_label.pack()
re_end_entry = tk.Entry(root)
re_end_entry.pack()

im_start_label = tk.Label(root, text="Imaginary Start:")
im_start_label.pack()
im_start_entry = tk.Entry(root)
im_start_entry.pack()

im_end_label = tk.Label(root, text="Imaginary End:")
im_end_label.pack()
im_end_entry = tk.Entry(root)
im_end_entry.pack()

generate_button = tk.Button(root, text="Generate Mandelbrot", command=lambda: [set_parameters(), generate_mandelbrot()])
generate_button.pack()

root.mainloop()
