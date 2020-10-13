def find(arrival_time, t):
    res = None
    ind = None
    for i in range(len(arrival_time)):
        if arrival_time[i]<=t and (res==None or res>arrival_time[i]):
            res = arrival_time[i]
            ind = i
    return ind

n = int(input("enter the number of processes: "))
times = []
arrival_time = []
burst_time = []
for i in range(n):
    arrival_time.append(int(input("enter arrival time of process " +str(i+1)+ ": ")))
for i in range(n):
    burst_time.append(int(input("enter burst time of process " +str(i+1)+ ": ")))
qt = int(input('enter quantum time: '))

burst_time_res = burst_time[:]
arrival_time_old = arrival_time[:]
indx = list(range(n))
turn_around = [0]*n
wait_time = [0]*n
exit_time = [0]*n
cs = 0
t = min(arrival_time)
reali = None

while arrival_time:
    ind = find(arrival_time, t)
    if ind==None:
        t+=1
        continue
    temp = indx[ind]
    if temp != reali and reali != None:
        cs+=1
    reali = temp
    if t>arrival_time[ind]:
        wait_time[reali] += t-arrival_time[ind]
    else:
        t = arrival_time[ind]
    arrival_time.pop(ind)
    if burst_time[ind]>qt:
        t += qt
        arrival_time.append(t)
        burst_time.append(burst_time.pop(ind) - qt)
        indx.append(indx.pop(ind))
    else:
        t += burst_time[ind]
        turn_around[reali] = t-arrival_time_old[reali]
        exit_time[reali] = t
        burst_time.pop(ind)
        indx.pop(ind)
    
print()
print('Process ID\t\tArrival Time\t\tBurst Time\t\tExit Time\t\tTurn Around Time\t\tWait time')
for i in range(n):
    print(i+1,'\t\t',arrival_time_old[i],'\t\t',burst_time_res[i],'\t\t',exit_time[i],'\t\t',turn_around[i],'\t\t',wait_time[i])
print()
print('average waiting time:', sum(wait_time)/n)
print('average turnaround time:', sum(turn_around)/n)
print('number of context switches:', cs)
