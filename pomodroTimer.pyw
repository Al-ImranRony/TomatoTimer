''' Default timer for pomodoro tracking '''

import time
import datetime as dt
import tkinter                                              # For GUI
from tkinter import messagebox                              # Ask for prompt & display messages
import winsound                                             # For Sound-play in windows

# Time informations
cur_time = dt.datetime.now()                                # Collect current time & date as datetime objects
pom_time = 25 * 60                                          # Pomodoro time
time_delta = dt.timedelta(0, pom_time)                      # Time difference in minits
pomEnd_time = cur_time + time_delta                         # Ending time of pomodoro
break_time = 5 * 60                                         # Break after a pomodoro    
final_time = cur_time + dt.timedelta(0,pom_time+break_time) # Final ending time-5 mins

# Pomodro GUI set
root = tkinter.Tk()                                         # Start new window
root.withdraw()                                             # Hide tkinter main window
messagebox.showinfo("Starting Pomodoro  >| ",
"\n Current time: "+cur_time.strftime("%H:%M %p") + 
". \n Timer is setting for 25 mins.")                       # Show alert messages

total_poms = 0                                              # Initialize Pomodoro counter
breaks = 0 
while True:
    if cur_time < pomEnd_time:
        print('pmodoro')
    elif pomEnd_time <= cur_time <= final_time:
        print('in break')                                   # Past Pomodoros within the break 
        if breaks == 0:                                     # Check if initial pomodoro 
            print('if break')
            for i in range(5):                              # If so, ring the bell
                winsound.Beep((i + 100), 700)
            print('Break time !')
            breaks += 1
    else:
        print('finished')
        # Pomodoro finished, reset breaks.
        breaks = 0
        for i in range(10):
            winsound.Beep((i+100), 500)
        response = messagebox.askyesno("Finished Pomodoro !","Would you like start again ?")
        total_poms += 1
        if response == True:
            cur_time = dt.datetime.now()
            pomEnd_time = cur_time + dt.timedelta(0, pom_time)
            final_time = cur_time + dt.timedelta(0, pom_time+break_time)
            continue
        elif response == False:
            messagebox.showinfo("Finished Pomodoro !", "\nYou completed "+str(total_poms)+" pomodoros today !")
            break
    
    print('Sleeping')                                       # To save memory    
    time.sleep(20)                                          # Check every 20 secs
    cur_time = dt.datetime.now()                            # And update time
    time_now = cur_time.strftime("%H:%M %p")

