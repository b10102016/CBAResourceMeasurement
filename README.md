# CBAResourceMeasurement
Container-based Android Resource Measurement
target : Memory, FPS, UI response time, First shutdown (cat kernel log first shutdown command)
## for CPU & memory
   Inspired from this [repo](https://github.com/moby/moby/blob/eb131c5383db8cac633919f82abad86c99bffbe5/cli/command/container/stats_helpers.go#L175-L188)
  Implemented by python 2.7.15
  lxc cgroup cpuacct in Android is incorect.
  So we cant measure CPU usage per container now..

  [Knowledge](https://hk.saowen.com/a/ae24edc5fd6546d47fcdbf38435d6e378a8cf6e778c14de1985eab803e0f949a) we need to know
## for GPU
https://www.jianshu.com/p/1fe9783d266b

