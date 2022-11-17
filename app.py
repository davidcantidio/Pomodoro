from tkinter import *
from config import *

menu = Tk()
menu.title("Pomodoro")
menu.geometry(f'{screen_max_width}x{screen_max_height}+{screen_pos_x}+{screen_pos_y}')
menu.resizable(True, True)
menu.minsize(int(screen_min_width), int(screen_min_height))
menu.maxsize(int(screen_max_width), int(screen_max_height))

#Icon setup
icon = PhotoImage(file="icon/pomodoro.png")
menu.tk.call('wm', 'iconphoto', menu._w, icon)
menu.iconphoto(False, icon)


#Start Button
btn_start = Button(menu, text = "start")
btn_reset = Button(menu, text = "reset")
btn_pause = Button(menu, text= "pause")
btn_start.pack()
btn_reset.pack()
btn_pause.pack()

menu.mainloop()