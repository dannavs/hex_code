import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from time import sleep

class PictureCodes(tk.Tk):
    def __init__(self):
        Tk.__init__(self)

        self.rgb_code = None
        self.pi = None
        self.px = None
        self.im = None
        self.user_pic_loc = None
        self.hex_code = ""

        self.title("Color Codes")
        self.app_width = 800
        self.app_height = 800
        self.x_cor = (0.5 * self.winfo_screenwidth()) - (0.5 * self.app_width)
        self.y_cor = (0.5 * self.winfo_screenheight()) - (0.5 * self.app_height)
        self.geometry('%dx%d+%d+%d' % (self.app_width, self.app_height, self.x_cor, self.y_cor))
        self.focus_force()

        self.frame_top = ttk.Frame(master=self, borderwidth=2, width=20)
        self.frame_top.grid(column=0, row=0)
        self.frame_bottom = ttk.Frame(master=self, borderwidth=2)
        self.frame_bottom.grid(column=0, row=1)

        self.open_but = ttk.Button(master=self.frame_top,  text='Open File', padding=20, command=self.open_and_sample)
        self.open_but.grid(column=0, row=0)
        self.title_inside = ttk.Label(master=self.frame_top, text="Hex Code Grabber", width=20, padding=20, font='helvetica 24')
        self.title_inside.grid(column=1, row=0)
        self.hex_code_label = ttk.Label(master=self.frame_top, text=f"Hex Code: {self.hex_code}", padding=20)
        self.hex_code_label.grid(column=2, row=0)
        self.user_pic_label = ttk.Label(master=self.frame_bottom, padding=5)
        self.user_pic_label.grid(column=0, row=0)

        self.mouse_x = 0
        self.mouse_y = 0
        # self.mouse_coords = Label(self)
        # self.mouse_coords.place(x=350, y=0)
        self.show_mouse_pos()

        # self.open_and_sample()
        while True:
            self.show_mouse_pos()
            if self.user_pic_loc:
                self.show_hex_value()
            self.update()
            sleep(0)


    def open_and_sample(self):
        self.user_pic_loc = filedialog.askopenfilename(title="Open Picture")
        if self.user_pic_loc:
            self.im = Image.open(self.user_pic_loc)
            print(self.im.format, self.im.size, self.im.mode)
            # print(self.im.getpixel((self.mouse_x, self.mouse_y)))
            self.px = self.im.load()
            self.im.thumbnail((800, 600))
            self.pi = ImageTk.PhotoImage(self.im)
            self.user_pic_label.config(image=self.pi)


    def show_mouse_pos(self):
        self.mouse_x = self.frame_bottom.winfo_pointerx() - self.frame_bottom.winfo_rootx()
        self.mouse_y = self.frame_bottom.winfo_pointery() - self.frame_bottom.winfo_rooty()
        # self.mouse_coords.config(text=f"{self.mouse_x}, {self.mouse_y}")


    def show_hex_value(self):
        try:
            self.rgb_code = self.im.getpixel((self.mouse_x, self.mouse_y))
            # print(self.rgb_code)
            # print(len(self.rgb_code))
            # print(type(self.rgb_code))
            if self.im.mode == 'RGB':
                self.hex_code = rgb_to_hex(self.rgb_code)
            elif self.im.mode == 'RGBA':
                self.rgb_code = self.rgb_code[:3]
                # print(self.rgb_code)
                self.hex_code = rgb_to_hex(self.rgb_code)
            else:
                self.hex_code = 'TROUBLE'
                # print(self.hex_code)
            self.hex_code_label.config(text=f"Hex Code: {self.hex_code}")
        except IndexError:
            pass

def rgb_to_hex(rgb_code):
    return '#%02x%02x%02x' % rgb_code


run_it = PictureCodes()
run_it.mainloop()








