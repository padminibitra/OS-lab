def exitTime(n,burst_time,exit_time):
    exit_time.append(burst_time[0]+arrival_time[0])
    for i in range(1,n):
        exit_time.append(exit_time[i-1]+burst_time[i])
    return exit_time

def turnArroundTime(n,exit_time,arrival_time,turn_arround):
    for i in range(0,n):
        turn_arround.append(exit_time[i]-arrival_time[i])
    return turn_arround

def waitingTime(n,turn_arround,burst_time,wait_time):
    for i in range(0,n):
        wait_time.append(turn_arround[i] - burst_time[i])
    return wait_time


n = int(input("Enter the no.of processes : "))
burst_time = []
arrival_time = []
exit_time = []
turn_arround = []
wait_time = []
for i in range(n):
    arrival_time.append(int(input('Enter the arrival time of process '+str(i)+' :')))
for i in range(n):
    inp = int(input('Enter the burst time of process '+str(i)+' :'))
    burst_time.append(inp)
exit_time = exitTime(n,burst_time,exit_time)
turn_arround = turnArroundTime(n,exit_time,arrival_time,turn_arround)
wait_time = waitingTime(n,turn_arround,burst_time,wait_time)
print()
print('Process ID\t\tArrival Time\t\tBurst Time\t\tExit Time\t\tTurn Around Time\t\tWait time')
for i in range(n):
    print(i+1,'\t\t',arrival_time[i],'\t\t',burst_time[i],'\t\t',exit_time[i],'\t\t',turn_arround[i],'\t\t',wait_time[i])
print()
print('Average Waiting Time is:',sum(wait_time)/n)
print('Avergae Turn around Time is:',sum(turn_arround)/n)