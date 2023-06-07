import time
import os

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = '{:02d}:{:02d}'.format(mins, secs)
        print(timer_display, end='\r')
        time.sleep(1)
        seconds -= 1

    os.system('afplay /System/Library/Sounds/Glass.aiff')  # 在 Mac 上播放提示音
