import tkinter as tk

points = [tuple(map(int, line.split(','))) for line in open(0)]

# Calculate bounds
xs = [p[0] for p in points]
ys = [p[1] for p in points]
min_x, max_x = min(xs), max(xs)
min_y, max_y = min(ys), max(ys)

# Canvas size and padding
canvas_width = 800
canvas_height = 800
padding = 20

# Scale to fit canvas
scale_x = (canvas_width - 2 * padding) / (max_x - min_x)
scale_y = (canvas_height - 2 * padding) / (max_y - min_y)
scale = min(scale_x, scale_y)

# Transform points to canvas coordinates
def transform(point):
    x = padding + (point[0] - min_x) * scale
    y = padding + (point[1] - min_y) * scale
    return (x, y)

transformed_points = [transform(p) for p in points]

# Create window
root = tk.Tk()
root.title("Canvas Viewer")
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# Draw polygon
canvas.create_polygon(transformed_points, outline='blue', fill='lightblue', width=1)

root.mainloop()

# The Render is a Christmas Bell shape