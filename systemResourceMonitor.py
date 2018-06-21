import utilitys
import os
import GPUMonitor
# GPUMonitor.dumpsys_gfxinfo("192.168.0.10","com.android.chrome","com.google.android.apps.chrome.Main -d https://stackoverflow.com/")
#GPUMonitor.dumpsys_gfxinfo("192.168.0.10","com.example.android.recyclerview",".MainActivity")
print "If dumpsys gfxinfo result is null, remember to run the following command:"
print "telnet ...# setprop debug.hwui.profile true"
print "telnet ...# setprop debug.choreographer.skipwarning 1 "
print "telnet ...# setprop ctl.restart surfaceflinger; setprop ctl.restart zygote"
print "After all, you need to reconnect adb."


GPUMonitor.dumpsys_gfxinfo("192.168.0.50","com.android.chrome","com.google.android.apps.chrome.Main -d http://wayou.github.io/t-rex-runner/")










