import telnetlib
import time
import socket

sleep = time.sleep # alias

def deviceShell(cmds,ip,time_out=10):
    tn = telnetlib.Telnet()
    
    try:
        tn = telnetlib.Telnet(ip , timeout=time_out)
        #tn.set_debuglevel(2)
        sleep(0.2)
        for cmd in cmds:
            tn.write(cmd+"\n")
            sleep(0.2)
            tn.read_until(":/ #",timeout=time_out)
        tn.write("exit\n")
        
    except socket.error as e:
        if format(e).find("No route to host"):
            print "No route to host "+ip
            
            return
        else:
            raise e
    finally:
        tn.close()

def deviceShellWithResp(cmd,ip,time_out=10):
    tn = telnetlib.Telnet()
    
    try:
        tn = telnetlib.Telnet(ip , timeout=time_out)
        #tn.set_debuglevel(2)
        response=tn.read_until(":/ #",timeout=time_out)
        sleep(0.2)
        tn.write(cmd+"\n")
        sleep(0.2)
        response=tn.read_until(":/ #",timeout=time_out)
        sleep(0.2)
        tn.write("exit\n")
        if response is None : return ""
        return response
    except socket.error as e:
        if format(e).find("No route to host"):
            print "No route to host "+ip
            return ""
        else:
            raise e
    finally:
        tn.close()
    return ""
