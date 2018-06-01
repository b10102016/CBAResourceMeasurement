_in = "cpu  65676 2217 47119 25440934 9340 0 2372 0 0 0\ncpu0 28208 645 23671 6311314 1860 0 2176 0 0 0"
totalClock=0
for i in _in.split('\n'):
    if i.find('cpu ') != -1:
        for j in i.split():
            if j=="cpu" : continue
            totalClock+=int(j)
        break
print _in+"\n"
print totalClock
        