# FIXME: This can't measure CPU per container.

import utilitys

CG_CPUACCT_PATH="/acct"

def get_CPUacct_cg(ip,cg_cpuacct_path,group_name):
    

    cat_cmd = "cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq ;cat {0}/{1}/cpuacct.usage; cat {0}/{1}/cpuacct.usage_percpu; cat {0}/{1}/cpuacct.stat ; cat /proc/stat".format(cg_cpuacct_path,group_name)
    
    cpuacct_raw_str=utilitys.deviceShellWithResp(cat_cmd,ip)
    #print cpuacct_raw_str
    
    return parse_cpuacct(cpuacct_raw_str)

import sys
nanoSecondsPerSecond = 1e9


def parse_cpuacct(rawstr):
    totalClock=0
    cg_cpuinfo_key=['cpu_usage','cpu_usage_percpu','cpu_stat','sys_cpu_usage']
    cg_cpuinfo=dict.fromkeys(cg_cpuinfo_key,0)
    for i,line in enumerate(rawstr.split('\n')):
        if   i ==1:
            #cur_cpu_clock=int(line)
            cur_cpu_clock=100
            print cur_cpu_clock
        elif i ==2:
            cg_cpuinfo['cpu_usage']=int(line)
        elif i ==3:
            cg_cpuinfo['cpu_usage_percpu']=[int(x) for x in line.split()]
        elif i ==4:
            tmp_line=line
        elif i ==5:
            tmp_line=tmp_line+line
            cpu_stat_str=tmp_line.split()
            cpu_stat = {cpu_stat_str[0]:cpu_stat_str[1],cpu_stat_str[2]:cpu_stat_str[3]}
            cg_cpuinfo['cpu_stat'] = cpu_stat
        elif line.find('cpu ') != -1:
            for j in line.split():
                if j=="cpu" : continue
                totalClock+=int(j)
            print totalClock
            cg_cpuinfo['sys_cpu_usage']=numpy.float64(totalClock*nanoSecondsPerSecond/cur_cpu_clock)
            break
            
    return cg_cpuinfo
    
import numpy


def caculateCPUPercent(prev_cg_cpuinfo,cg_cpuinfo):

    print cg_cpuinfo
	
    cpuPercent = 0.0
    # calculate the change for the cpu usage of the container in between readings
    cpuDelta = float(cg_cpuinfo['cpu_usage']) - float(prev_cg_cpuinfo['cpu_usage'])
    # calculate the change for the entire system between readings
    systemDelta = float(cg_cpuinfo['sys_cpu_usage']) - float(prev_cg_cpuinfo['sys_cpu_usage'])


    if systemDelta > 0.0 and cpuDelta > 0.0:
	    cpuPercent = (cpuDelta / systemDelta) * len(prev_cg_cpuinfo['cpu_usage_percpu']) * 100.0
	
    return cpuPercent


import time

#cg_cpuinfo = get_CPUacct_cg("192.168.0.10",CG_CPUACCT_PATH,"lxc/con1")
cg_cpuinfo = get_CPUacct_cg("192.168.0.10",CG_CPUACCT_PATH,"")
while True:
    previous_cg=cg_cpuinfo
    cg_cpuinfo = get_CPUacct_cg("192.168.0.10",CG_CPUACCT_PATH,"")
    print caculateCPUPercent(previous_cg,cg_cpuinfo)
    time.sleep(5)