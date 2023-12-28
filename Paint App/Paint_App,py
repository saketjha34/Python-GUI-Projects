import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import ImageGrab

class PaintApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Paint Application")

        # Set up canvas
        self.canvas = tk.Canvas(self.master, bg="white", width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Brush settings
        self.brush_color = "black"
        self.eraser_color = "white"  # Transparent color for eraser
        self.brush_size = 2
        self.eraser_size_factor = 5
        self.last_x = 0
        self.last_y = 0
        self.draw_enabled = False
        self.eraser_mode = False

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Menu Bar
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        # File Menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_artwork)
        file_menu.add_command(label="Exit", command=self.master.destroy)

        # Color Button
        color_button = tk.Button(self.master, text="Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=5)

        # Brush Button
        brush_button = tk.Button(self.master, text="Brush", command=self.set_brush_mode)
        brush_button.pack(side=tk.LEFT, padx=5)

        # Eraser Button
        eraser_button = tk.Button(self.master, text="Eraser", command=self.set_eraser_mode)
        eraser_button.pack(side=tk.LEFT, padx=5)

        # Brush Size Scale
        self.brush_size_scale = tk.Scale(self.master, from_=1, to=10, orient=tk.HORIZONTAL, label="Brush Size", command=self.set_brush_size)
        self.brush_size_scale.pack(side=tk.LEFT, padx=5)
        self.brush_size_scale.pack_forget()

        # Eraser Size Scale
        self.eraser_size_scale = tk.Scale(self.master, from_=1, to=10, orient=tk.HORIZONTAL, label="Eraser Size", command=self.set_eraser_size)
        self.eraser_size_scale.pack(side=tk.LEFT, padx=5)
        self.eraser_size_scale.pack_forget()

        # Clear Canvas Button
        clear_button = tk.Button(self.master, text="Clear Canvas", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=5)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

        self.canvas.bind("<Button-3>", self.start_eraser)
        self.canvas.bind("<B3-Motion>", self.erase)
        self.canvas.bind("<ButtonRelease-3>", self.stop_drawing)

    def choose_color(self):
        if not self.eraser_mode:
            color = colorchooser.askcolor()[1]
            if color:
                self.brush_color = color

    def set_brush_mode(self):
        self.eraser_mode = False
        self.show_brush_settings()
        self.hide_eraser_settings()

    def set_eraser_mode(self):
        self.eraser_mode = True
        self.show_eraser_settings()
        self.hide_brush_settings()

    def set_brush_size(self, size):
        self.brush_size = int(size)

    def set_eraser_size(self, size):
        self.eraser_size = int(size)
        self.eraser_size *= self.eraser_size_factor

    def start_drawing(self, event):
        if not self.eraser_mode:
            self.draw_enabled = True
            self.last_x, self.last_y = event.x, event.y

    def paint(self, event):
        if self.draw_enabled and not self.eraser_mode:
            x, y = event.x, event.y
            size = self.eraser_size if self.eraser_mode else self.brush_size
            color = self.eraser_color if self.eraser_mode else self.brush_color
            self.canvas.create_line(self.last_x, self.last_y, x, y, width=size, fill=color, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.last_x, self.last_y = x, y

    def start_eraser(self, event):
        if self.eraser_mode:
            self.draw_enabled = True
            self.last_x, self.last_y = event.x, event.y

    def erase(self, event):
        if self.draw_enabled and self.eraser_mode:
            x, y = event.x, event.y
            size = self.eraser_size
            self.canvas.create_line(self.last_x, self.last_y, x, y, width=size, fill=self.eraser_color, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.last_x, self.last_y = x, y

    def stop_drawing(self, event):
        self.draw_enabled = False

    def clear_canvas(self):
        self.canvas.delete("all")

    def save_artwork(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            # Save the canvas as an image using PIL
            x0 = self.canvas.winfo_rootx()
            y0 = self.canvas.winfo_rooty()
            x1 = x0 + self.canvas.winfo_width()
            y1 = y0 + self.canvas.winfo_height()
            ImageGrab.grab().crop((x0, y0, x1, y1)).save(file_path)

    def show_brush_settings(self):
        self.brush_size_scale.pack()

    def hide_brush_settings(self):
        self.brush_size_scale.pack_forget()

    def show_eraser_settings(self):
        self.eraser_size_scale.pack()

    def hide_eraser_settings(self):
        self.eraser_size_scale.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()