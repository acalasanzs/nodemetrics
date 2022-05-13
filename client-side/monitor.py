import psutil                   # Monitor CPU, MEM and DISK
from sys import platform        # Check platform
from time import sleep          # For the interval
import GPUtil                   # GPU usage

interval = 0.5                 # Interval in seconds
statistics = dict()             # Object to send
resume = ["cpu","mem","disk","gpu"] # All subproperties
for prop in resume:
    statistics[prop] = dict()       # Create a new object inside the main object statistics
is_windows = True if platform == 'win32' else False # Boolean if It's windows
system = "Windows" if is_windows else "Linux" if platform in ["linux", "linux2"] else "MacOS" if platform == "darwin" else "unknown" # Check platform
primary_disk = 'C:\\' if is_windows else '/'    # Main disk
gpu_s = len(GPUtil.getAvailable(order = 'first', limit = 1, maxLoad = 0.5, maxMemory = 0.5, includeNan=False, excludeID=[], excludeUUID=[])) # How many dedicated GPU are there
def update():
    statistics["os"] = system

    """ CPU USAGE """
    statistics["cpu"]["count"] = psutil.cpu_count()
    statistics["cpu"]["percent"] = psutil.cpu_percent(interval=interval)

    """ MEMORY USAGE """
    statistics["mem"]["percent"] = psutil.virtual_memory().percent

    """ DISK USAGE """
    statistics["disk"]["partition"] = primary_disk
    statistics["disk"]["percent"] = psutil.disk_usage(primary_disk).percent

    """ GPU USAGE """
    if gpu_s > 0:
        statistics["gpu"]["percent"] = GPUtil.getGPUs()[0].load * 100


if __name__ == "__main__":
    update()
    while True:
        update()
        print(statistics)
        sleep(interval)

