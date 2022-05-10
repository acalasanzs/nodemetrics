import psutil
import sys
from time import sleep
import GPUtil
interval = 0.25
statistics = dict()
is_windows = True if sys.platform == 'win32' else False
system = "Windows" if is_windows else "Linux" if sys.platform in ["linux", "linux2"] else "MacOS" if sys.platform == "darwin" else "unknown"
primary_disk = 'C:\\' if is_windows else '/'
gpu_s = len(GPUtil.getAvailable(order = 'first', limit = 1, maxLoad = 0.5, maxMemory = 0.5, includeNan=False, excludeID=[], excludeUUID=[]))
def update():
    statistics["os"] = system

    """ CPU USAGE """
    statistics["cpu", "count"] = psutil.cpu_count()
    statistics["cpu", "percent"] = psutil.cpu_percent(interval=interval)

    """ MEMORY USAGE """
    statistics["mem", "percent"] = psutil.virtual_memory().percent

    """ DISK USAGE """
    statistics["disk", "partition"] = primary_disk
    statistics["disk", "usage"] = psutil.disk_usage(primary_disk).percent

    """ GPU USAGE """
    statistics["GPU", "COUNT"] = gpu_s
    statistics["GPU", "PERCENT"] = GPUtil.getGPUs()[0].load * 100

if __name__ == "__main__":
    update()
    while True:
        update()
        print(statistics)
        sleep(interval)

