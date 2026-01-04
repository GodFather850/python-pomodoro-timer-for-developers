import time
import os

timer = float(input("how can today? "))
if timer < 5 and timer > 0:
    seconds = 0
    miniutes = 0
    for i in range(0, timer):
        while seconds == time * 3600:
            os.system("clear")
            seconds = seconds + 1
            print(seconds)
            time.sleep(1)
            if seconds == 60:
                miniutes = 1
                if miniutes == 25:
                    os.system('notify-send "Time to have some tea or coffee and rest for a few minutes. Don't be tired"')
else:
    os.system("clear")
    exit("Err: hour is not authentic")
