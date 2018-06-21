# CBAResourceMeasurement
Container-based Android Resource Measurement
target : Memory, FPS, UI response time, First shutdown (cat kernel log first shutdown command)
## for CPU & memory
   Inspired from this [repo](https://github.com/moby/moby/blob/eb131c5383db8cac633919f82abad86c99bffbe5/cli/command/container/stats_helpers.go#L175-L188)
  Implemented by python 2.7.15

  The lxc's cpuacct group setting will be overrided by android's cpuacct cgroup
  lxc cgroup cpuacct in Android is grouped by application's uid.
  
  So we can't measure CPU usage per container for now..

  CPU Shares 控制下限
  CFS_quota 控制上限


  



  [Knowledge](https://hk.saowen.com/a/ae24edc5fd6546d47fcdbf38435d6e378a8cf6e778c14de1985eab803e0f949a) we need to know
## for GPU
write a simple recyclerview program for measure GPU FPS

setprop debug.hwui.profile true 
to get more GPU info in dumpsys
https://www.jianshu.com/p/1fe9783d266b


setprop debug.choreographer.skipwarning 1
setprop ctl.restart surfaceflinger; setprop ctl.restart zygote
to get dropped frame info
http://xuxu1988.com/2016/04/30/gt-sm-test/


`utilitys.dumpsys_gfxinfo` This can only use above Android 6.0, and we are in Android 5.1.1......

# Measurement target
- 掉禎數
- 禎數
- dd測試
- 
aapt dump badging for getting MainActivity intent






