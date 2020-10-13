def findall(arrival_time, t):
    res = []
    for i in range(len(arrival_time)):
        if arrival_time[i]<=t:
            res.append(i)
    return res

def find(burst_time, indices):
    ans = indices[0]
    m = burst_time[ans]
    for i in indices[1:]:
        if m>burst_time[i]:
            m = burst_time[i]
            ans = i
    return ans

n = int(input("enter the number of processes: "))
arrival_time = []
burst_time = []
for i in range(n):
    arrival_time.append(int(input("enter arrival time of process " +str(i+1)+ ": ")))
for i in range(n):
    burst_time.append(int(input("enter burst time of process " +str(i+1)+ ": ")))
#sjf start
indx = list(range(n))
burst_time_res = burst_time[:]
arrival_time_res = arrival_time[:]
turn_around = [0]*n
wait_time = [0]*n
exit_time = turn_around[:]
cs = 0
reali=None
t = min(arrival_time)
while arrival_time:
    indices = findall(arrival_time, t)
    ind = find(burst_time, indices)
    temp = indx[ind]
    if temp != reali and reali != None:
        cs += 1
    reali = temp
    for i in indices:
        wait_time[indx[i]] += 1
    wait_time[reali] -= 1
    burst_time[ind] -= 1
    t += 1
    if burst_time[ind]==0:
        turn_around[reali] = t-arrival_time[ind]
        exit_time[reali] = t
        arrival_time.pop(ind)
        burst_time.pop(ind)
        indx.pop(ind)
        
#sjf end
print()
print('Process ID\t\tArrival Time\t\tBurst Time\t\tExit Time\t\tTurn Around Time\t\tWait time')
for i in range(n):
    print(i+1,'\t\t',arrival_time_res[i],'\t\t',burst_time_res[i],'\t\t',exit_time[i],'\t\t',turn_around[i],'\t\t',wait_time[i])
print()
print('average waiting time:', sum(wait_time)/n)
print('average turnaround time:', sum(turn_around)/n)
print('number of context switches:', cs)

