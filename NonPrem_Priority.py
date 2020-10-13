def findall(arrival_time, t):
    res = []
    for i in range(len(arrival_time)):
        if arrival_time[i]<=t:
            res.append(i)
    return res

def find(p, indices):
    ans = indices[0]
    m = p[ans]
    for i in indices[1:]:
        if m>p[i]:
            m = p[i]
            ans = i
    return ans

n = int(input("enter the number of processes: "))
arrival_time = []
burst_time = []
priority = []
for i in range(n):
    arrival_time.append(int(input("enter arrival time of process " +str(i+1)+ ": ")))
for i in range(n):
    burst_time.append(int(input("enter burst time of process " +str(i+1)+ ": ")))
for i in range(n):
    priority.append(int(input("enter priority of process " +str(i+1)+ ": ")))

#sjf non preemtive start
burst_time_res = burst_time[:]
arrival_time_res = arrival_time[:]
indx = [i for i in range(n)]
p = [0]*n
turn_around = [0]*n
wait_time = turn_around[:]
exit_time = turn_around[:]
cs = n-1
t = min(arrival_time)
while arrival_time:
    indices = findall(arrival_time, t)
    ind = find(p, indices)
    currarrival_time = arrival_time.pop(ind)
    currburst_time = burst_time.pop(ind)
    currp = p.pop(ind)
    reali = indx.pop(ind)
    if t>currarrival_time:
        wait_time[reali] = t-currarrival_time
    else:
        wait_time[reali] = 0
        t = currarrival_time
    t += currburst_time
    turn_around[reali] = t-currarrival_time
    exit_time[reali] = t
#sjf ends

print()
print('Process ID\t\tPriority\t\tArrival Time\t\tBurst Time\t\tExit Time\t\tTurn Around Time\t\tWait time')
for i in range(n):
    print(i+1,'\t\t',priority[i],'\t\t',arrival_time_res[i],'\t\t',burst_time_res[i],'\t\t',exit_time[i],'\t\t',turn_around[i],'\t\t',wait_time[i])
print()

print()
print('average waiting time:', sum(wait_time)/n)
print('average turnaround time:', sum(turn_around)/n)
print('number of context switches:', cs)


