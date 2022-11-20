import tkinter as tk
from config import *
from tkfontawesome import icon_to_image
import time

class App(tk.Tk):
    def startWorkTimer(self, remaining_secs, remaining_minutes):
        mins = int(remaining_minutes.get())
        secs = int(remaining_secs.get())
        while int(mins) > 0:
            while int(secs) > 0 and mins > 0:
                secs-= 1
                remaining_secs.set(secs)
                time.sleep(1)
                print(secs)
                self.update()
            mins -= 1
            remaining_minutes.set(mins)
            secs = 60
        #     remaining_secs.set(59)
        #     chosen_work_minutes.set(chosen_work_minutes.get()-1)
        #     
        # elif remaining_secs.get() == 0 and chosen_work_minutes.get()  == 0:
        #     tk.messagebox.showinfo("Time Countdown", "Time's up ")
        # else:
        #     remaining_secs.set(remaining_secs.get()-1)
        #     time.sleep(1)

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
        
        #creating main containers
        settings_frame = tk.Frame(self, bg='pink')
        settings_frame.place(x=10, y=10)
        periods_frame = tk.Frame(settings_frame, bg='yellow')
        periods_frame.pack(side = 'left')
        cicles_frame = tk.Frame(settings_frame, bg='red')
        cicles_frame.pack(side = 'right', fill='y')
        display_frame = tk.Frame(self, bg="red")
        display_frame.place(x=10, y=250)
        controls_frame = tk.Frame(self, bg="blue")
        controls_frame.place(x=500, y=10, height=100)

        #Define amd display chosen working period in minutes
        self.chsn_wrk_mins = tk.StringVar(display_frame)
        self.work_mins_entry = tk.Scale(periods_frame, variable=self.chsn_wrk_mins, from_=work_scale_min, to=work_scale_max, resolution=5, orient='horizontal', label='Trabalho (min)', length=270)


        self.work_mins_entry.pack(padx=5, pady=2, side='top', fill='x')
        self.wrk_mins_label = tk.Label(display_frame, textvariable=self.chsn_wrk_mins)
        self.wrk_mins_label.grid(row=0, column=0)
        self.remaining_secs = tk.StringVar(display_frame, "60")
        self.wrk_rmng_secs_label = tk.Label(display_frame, textvariable=self.remaining_secs)

        self.wrk_rmng_secs_label.grid(row=0, column=2)


        #Define and display the period in minutes of the small break
        self.chsn_sm_brk_mins = tk.StringVar(display_frame)
        self.sm_brk_mins_entry = tk.Scale(periods_frame, variable=self.chsn_sm_brk_mins, from_=sm_break_min, to=sm_break_max, resolution=5, orient='horizontal', label='Pausa menor', length=270)
        self.sm_brk_mins_entry.pack(padx=5, pady=2, side='top', fill='x')
        self.sm_brk_mins_label = tk.Label(display_frame, textvariable=self.chsn_sm_brk_mins)
        self.sm_brk_mins_label.grid(row=0, column=3)

        #Define the period in minutes of the big break
        self.chsn_bg_brk_mins = tk.StringVar(display_frame)
        self.bg_brk_mins_entry = tk.Scale(periods_frame, variable=self.chsn_bg_brk_mins, from_=bg_break_min, to=bg_break_max, resolution=5, orient='horizontal', label='Pausa maior', length=270)
        self.bg_brk_mins_entry.pack(padx=5, pady=2, side='top', fill='x')
        self.bg_brk_mins_label = tk.Label(display_frame, textvariable=self.chsn_bg_brk_mins)
        self.bg_brk_mins_label.grid(row=0, column=4)


        self.cicles_n_entry = tk.StringVar(display_frame)
        self.bg_break_mins_entry = tk.Scale(cicles_frame, from_=cicles_min, to=cicles_max, resolution=1, orient='vertical', label='Ciclos', length=190)
        self.bg_break_mins_entry.pack(padx=5, pady=2, side='top', fill='x')

    



            #Buttons
                #Play/Pause button
        self.btn_playpause_icon = icon_to_image("play", fill="#3a3b3c", scale_to_width=15) 
        self.btn_playpause= tk.Button(controls_frame, image = self.btn_playpause_icon, width=30, height=30, command=lambda: self.startWorkTimer(self.remaining_secs, self.chsn_wrk_mins))
        self.btn_playpause.pack(padx=5, pady=2)  

                #Reset Button
        self.btn_reset_icon = icon_to_image("history", fill="#3a3b3c", scale_to_width=15)
        self.btn_reset = tk.Button(controls_frame, image = self.btn_reset_icon, width=30, height=30)
        self.btn_reset.pack(padx=5, pady=2)
        
    

                # Declaration of variables
        
    


    def currentTask(self):
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