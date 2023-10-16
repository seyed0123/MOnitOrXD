import psutil
import GPUtil
import cpuinfo


# Function to check CPU usage
def check_cpu_usage(threshold=50):
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_info = cpuinfo.get_cpu_info()
    if cpu_usage > threshold:
        return str(f"High CPU usage detected: {cpu_usage}%")
    else:
        return [
            str(f"CPU usage : {cpu_usage}% "),
            str(f"CPU model: {cpu_info['brand_raw']} , number of CORS: {cpu_info['count']}, ")]


# Function to check memory usage
def check_memory_usage(threshold=80):
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > threshold:
        return str(f"High memory usage detected: {memory_usage}%")
    else:
        return str(f"memory usage: {memory_usage}%")


# Function to check disk space
def check_disk_space(threshold=90):
    ret = []
    disks = psutil.disk_partitions(all=False)
    for disk in disks:
        if disk.opts == 'cdrom':
            continue
        path = disk.device
        disk_usage = psutil.disk_usage(path)
        disk_type = disk.fstype
        ret.append(str(
            f"Disk name:{path[0:2]},disk free:{round(disk_usage.free / 1024 ** 3,2)}  GB ,Disk usage: {disk_usage.percent}% , "
            f"Disk FS type{disk_type}"))
    return ret


# Function to check network traffic
def check_network_traffic(threshold=100 * 1024 * 1024):
    network_traffic = psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent
    if network_traffic > threshold:
        return str(f"High network traffic detected: {network_traffic} MB")
    else:
        return str(f"network traffic: {network_traffic} MB")


def check_battery():
    battery = psutil.sensors_battery()
    return str(f"Battery charge:{battery.percent}% , charging:{battery.power_plugged} ")


def get_gpu_temperature():
    gpus = GPUtil.getGPUs()
    gpu = gpus[0]
    return [str(f"GPU model :{gpu.name}"),
            str(f"memory Free:{gpu.memoryFree / 1024} GB , memory usage:{(gpu.memoryUsed / gpu.memoryTotal) * 100}% , GPU temperature: {gpu.temperature}")]


# Function to run health checks
def run_health_checks():
    print("Monitoring the system...")
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    gpu = get_gpu_temperature()
    battery = check_battery()
    network = check_network_traffic()
    static = [cpu[1], *check_disk_space(), gpu[0]]
    dynamic = [cpu[0], memory, network, battery, gpu[1]]

    return [*static, *dynamic]
