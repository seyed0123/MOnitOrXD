import psutil
import GPUtil

# Function to check CPU usage
def check_cpu_usage(threshold=50):
    cpu_usage = psutil.cpu_percent(interval=1)

    if cpu_usage > threshold:
        print(f"High CPU usage detected: {cpu_usage}%")
    else:
        print(f"CPU usage : {cpu_usage}%")


# Function to check memory usage
def check_memory_usage(threshold=80):
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > threshold:
        print(f"High memory usage detected: {memory_usage}%")
    else:
        print(f"memory usage: {memory_usage}%")


# Function to check disk space
def check_disk_space(threshold=90):
    disks = psutil.disk_partitions(all=False)
    for disk in disks:
        if disk.opts == 'cdrom':
            continue
        path = disk.device
        disk_usage = psutil.disk_usage(path)
        disk_type = disk.fstype
        print(
            f"Disk name:{path[0:2]},disk free:{disk_usage.free / 1024 ** 3}  GB ,Disk usage: {disk_usage.percent}% , "
            f"Disk FS type{disk_type}")


# Function to check network traffic
def check_network_traffic(threshold=100 * 1024 * 1024):
    network_traffic = psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent
    if network_traffic > threshold:
        print(f"High network traffic detected: {network_traffic:.2f} MB")
    else:
        print(f"network traffic: {network_traffic:.2f} MB")


def check_gpu_usage(threshold=50):
    gpu_usage = psutil.virtual_memory()

    if gpu_usage > threshold:
        print(f"High gpu usage detected: {gpu_usage}%")
    else:
        print(f"gpu usage : {gpu_usage}%")


def check_battery():
    battery = psutil.sensors_battery()
    print(f"Battery charge:{battery.percent}% , charging:{battery.power_plugged} ")


def get_gpu_temperature():
    gpus = GPUtil.getGPUs()
    gpu = gpus[0]
    print(f"GPU model :{gpu.name}, memory Free:{gpu.memoryFree/1024} GB , memory usage:{(gpu.memoryUsed/gpu.memoryTotal)*100}% , GPU temperature: {gpu.temperature}")

# Function to run health checks
def run_health_checks():

    print("Monitoring the system...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    get_gpu_temperature()
    check_network_traffic()
    check_battery()
