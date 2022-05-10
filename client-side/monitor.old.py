import os
import subprocess
import re

import shutil

from time import sleep


""" CPU USAGE """

statistics = {}

# Get Physical and Logical CPU count
statistics['physical_and_logical_cpu_count'] = os.cpu_count()
statistics['cpu_load'] = [x / os.cpu_count() * 100 for x in os.getloadavg()][-1]

""" RAM USAGE """

matcher = re.compile('\d+')

# Memory usage
total_ram = subprocess.run(['sysctl', 'hw.memsize'], stdout=subprocess.PIPE).stdout.decode('utf-8')
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
vmLines = vm.split('\n')

wired_memory = (int(matcher.search(vmLines[6]).group()) * 4096) / 1024 ** 3
free_memory = (int(matcher.search(vmLines[1]).group()) * 4096) / 1024 ** 3
active_memory = (int(matcher.search(vmLines[2]).group()) * 4096) / 1024 ** 3
inactive_memory = (int(matcher.search(vmLines[3]).group()) * 4096) / 1024 ** 3

# Used memory = wired_memory + inactive + active

statistics['ram'] = dict({
    'total_ram': int(matcher.search(total_ram).group())/1024**3,
    'used_ram': round(wired_memory+active_memory+inactive_memory, 2),
})

""" DISK USAGE """

# Top command on mac displays and updates sorted information about processes.

top_command = subprocess.run(['top', '-l 1', '-n 0'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')

# Disk usage
# Get total disk size, used disk space, and free disk

total, used, free = shutil.disk_usage("/")

# Number of Read and write operations
# from the top command, the read written result will be as follows
# 'Disks: XXXXXX/xxG read, XXXX/xxG written.'
# we thus need to extract the read and written from this.
read_written = top_command[9].split(':')[1].split(',')
read = read_written[0].split(' ')[1]
written = read_written[1].split(' ')[1]

statistics['disk'] = dict(
    {
        'total_disk_space': round(total / 1024 ** 3, 1),
        'used_disk_space': round(used / 1024 ** 3, 1),
        'free_disk_space': round(free / 1024 ** 3, 1),
        'read_write': {
            'read': read,
            'written': written
        }
    }
)

""" NETWORK LATENCY """
"""
Here we will ping google at an interval of five seconds for five times and record the
min response time, average response time, and the max response time. 
"""
ping_result = subprocess.run(['ping', '-i 5', '-c 5', 'google.com'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')

min, avg, max = ping_result[-2].split('=')[-1].split('/')[:3]
statistics['network_latency'] = dict(
    {
        'min': min.strip(),
        'avg': avg.strip(),
        'max': max.strip(),
    }
)

while True:
    print(statistics)
    sleep(500)