from tkinter import *
from config import *

menu = Tk()
menu.title("Pomodoro")
menu.geometry(f'{screen_max_width}x{screen_max_height}+{screen_pos_x}+{screen_pos_y}')
menu.resizable(True, True)
menu.minsize(int(screen_min_width), int(screen_min_height))
menu.maxsize(int(screen_max_width), int(screen_max_height))
menu.iconbitmap("icon/pomodoro.ico")
menu.mainloop()