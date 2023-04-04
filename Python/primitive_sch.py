class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

class Scheduler:
    def __init__(self, processes):
        self.processes = processes
    
    def schedule(self):
        current_time = 0
        waiting_time = {}
        turnaround_time = {}
        for p in self.processes:
            waiting_time[p.pid] = 0
            turnaround_time[p.pid] = p.burst_time
            current_time += p.burst_time
    
        avg_waiting_time = sum(waiting_time.values()) / len(waiting_time)
        avg_turnaround_time = sum(turnaround_time.values()) / len(turnaround_time)
        print("Average Waiting Time:", avg_waiting_time)
        print("Average Turnaround Time:", avg_turnaround_time)
