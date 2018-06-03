import utilitys
import os

os.system("adb -s 192.168.0.10 shell am start com.android.chrome/com.google.android.apps.chrome.Main -d https://stackoverflow.com/")
utilitys.dumpsys_gfxinfo("192.168.0.10","com.android.chrome","com.google.android.apps.chrome.Main -d https://stackoverflow.com/")







