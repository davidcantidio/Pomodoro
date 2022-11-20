import tkinter as tk
from config import *
from tkfontawesome import icon_to_image

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.geometry(f'{screen_max_width}x{screen_max_height}+{screen_pos_x}+{screen_pos_y}')
        self.resizable(True, True)
        self.minsize(screen_min_width, screen_min_height)
        self.maxsize(screen_max_width, screen_max_height)
        # #Icon setup
        icon = icon_to_image("clock", fill="#3a3b3c", scale_to_width=45)
        self.iconphoto(False, icon)
        
        #creating a container 
        settings_frame = tk.Frame(self, bg='pink')
        settings_frame.place(x=10, y=10)
        periods_frame = tk.Frame(settings_frame, bg='yellow')
        periods_frame.pack(side = 'left')

        self.chsn_wrk_mins = tk.StringVar()
        self.work_mins_entry = tk.Scale(periods_frame, variable=self.chsn_wrk_mins, from_=work_scale_min, to=work_scale_max, resolution=5, orient='horizontal', label='Trabalho (min)', length=270)
        self.work_mins_entry.pack(padx=5, pady=2, side='top', fill='x')

        self.sm_break_mins_entry = tk.StringVar()
        self.sm_break_mins_entry = tk.Scale(periods_frame, from_=sm_break_min, to=sm_break_max, resolution=5, orient='horizontal', label='Pausa menor', length=270)
        self.sm_break_mins_entry.pack(padx=5, pady=2, side='top', fill='x')
        
        self.bg_break_mins_entry = tk.StringVar()
        self.bg_break_mins_entry = tk.Scale(periods_frame, from_=bg_break_min, to=bg_break_max, resolution=5, orient='horizontal', label='Pausa maior', length=270)
        self.bg_break_mins_entry.pack(padx=5, pady=2, side='top', fill='x')

        cicles_frame = tk.Frame(settings_frame, bg='red')
        cicles_frame.pack(side = 'right', fill='y')
        self.cicles_n_entry = tk.StringVar()
        self.bg_break_mins_entry = tk.Scale(cicles_frame, from_=cicles_min, to=cicles_max, resolution=1, orient='vertical', label='Ciclos', length=190)
        self.bg_break_mins_entry.pack(padx=5, pady=2, side='top', fill='x')

        controls_frame = tk.Frame(self, bg="blue")
        controls_frame.place(x=500, y=10, height=100)
            #Buttons
                #Play/Pause button
        self.btn_playpause_icon = icon_to_image("play", fill="#3a3b3c", scale_to_width=15)
        
        self.btn_playpause= tk.Button(controls_frame, image = self.btn_playpause_icon, width=30, height=30, command=print("timer"))
        self.btn_playpause.pack(padx=5, pady=2)  

                #Reset Button
        self.btn_reset_icon = icon_to_image("history", fill="#3a3b3c", scale_to_width=15)
        self.btn_reset = tk.Button(controls_frame, image = self.btn_reset_icon, width=30, height=30)
        self.btn_reset.pack(padx=5, pady=2)

        display_frame = tk.Frame(self, bg="red")
        display_frame.place(x=10, y=450)

        self.chsn_wrk_mins.set(f'{str(self.chsn_wrk_mins)} mins.')
        self.wrk_mins_label = tk.Label(display_frame, textvariable=self.text)
        self.wrk_mins_label.pack(side='right')

                # Declaration of variables
        



    def currentTask(self):
        pass

    def startTimer(self):
        pass

# def submit():
#     try:
#         # the input provided by the user is
#         # stored in here :temp
#         temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
#     except:
#         print("Please input the right value")
#     while temp >-1:
         
#         # divmod(firstvalue = temp//60, secondvalue = temp%60)
#         mins,secs = divmod(temp,60)
  
#         # Converting the input entered in mins or secs to hours,
#         # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
#         # 50min: 0sec)
#         hours=0
#         if mins >60:
             
#             # divmod(firstvalue = temp//60, secondvalue
#             # = temp%60)
#             hours, mins = divmod(mins, 60)
         
#         # using format () method to store the value up to
#         # two decimal places
#         hour.set("{0:2d}".format(hours))
#         minute.set("{0:2d}".format(mins))
#         second.set("{0:2d}".format(secs))
  
#         # updating the GUI window after decrementing the
#         # temp value every time
#         root.update()
#         time.sleep(1)
  
#         # when temp value = 0; then a messagebox pop's up
#         # with a message:"Time's up"
#         if (temp == 0):
#             messagebox.showinfo("Time Countdown", "Time's up ")
         
#         # after every one sec the value of temp will be decremented
#         # by one
#         temp -= 1
 
# # button widget
# btn = Button(root, text='Set Time Countdown', bd='5',
#              command= submit)
# btn.place(x = 70,y = 120)
  
# # infinite loop which is required to
# # run tkinter program infinitely
# # until an interrupt occurs

if __name__== "__main__":
    app = App()
    app.mainloop()