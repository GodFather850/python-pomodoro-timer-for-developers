import time
import os

# input hour
timer = float(input("how can today? "))
if timer < 5 and timer > 0:
    seconds = 0
    miniutes = 0
    for i in range(0, timer): # loop for calculate time
        while seconds == time * 3600: # calculate time for send notification
            os.system("clear")
            seconds = seconds + 1
            print(seconds)
            time.sleep(1) # Delay
            if seconds == 60: # calculate miniutes
                miniutes = miniutes + 1
                if miniutes == 25: # Send Notf
                    os.system('notify-send "Time to have some tea or coffee and rest for a few minutes. Don't be tired"')
else:
    os.system("clear")
    exit("Err: hour is not authentic")
