import os
import time
try:
    while True:
        os.system("adb -s 192.168.3.10 shell input keyevent KEYCODE_APP_SWITCH")
        time.sleep(0.1)
except KeyboardInterrupt:
    exit()
