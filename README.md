# CBAResourceMeasurement
Container-based Android Resource Measurement
target : Memory, FPS, UI response time, First shutdown (cat kernel log first shutdown command)
## for CPU & memory
   Inspired from this [repo](https://github.com/moby/moby/blob/eb131c5383db8cac633919f82abad86c99bffbe5/cli/command/container/stats_helpers.go#L175-L188)
  Implemented by python 2.7.15

  The lxc's cpuacct group setting will be overrided by android's cpuacct cgroup
  lxc cgroup cpuacct in Android is grouped by application's uid.
  
  So we can't measure CPU usage per container for now..


  [Knowledge](https://hk.saowen.com/a/ae24edc5fd6546d47fcdbf38435d6e378a8cf6e778c14de1985eab803e0f949a) we need to know
## for GPU
write a simple recyclerview program for measure GPU FPS

https://www.jianshu.com/p/1fe9783d266b




