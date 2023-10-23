import os
import time

import plotille
import psutil
import GPUtil
import cpuinfo
import numpy as np

time_arr = np.array([0])
cpu_arr = np.array([0])
ram_arr = np.array([0])
network_arr = np.array([0])
gpu_arr = np.array([0])
battery_arr = np.array([0])
bef_time = 0
clear = lambda: os.system('clear')

def plot(x, y, X_label, Y_label):
    print(plotille.plot(y, x,  Y_label=X_label, X_label=Y_label, height=5, width=90, x_min=0, y_min=0, lc=150, bg=60,
                        color_mode='byte'))
    return str(
        plotille.plot(x, y, X_label=X_label, Y_label=Y_label, height=10, width=90, x_min=0, y_min=0, lc=150, bg=60,
                      color_mode='byte'))


# Function to check CPU usage
def check_cpu_usage(threshold=50):
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_info = cpuinfo.get_cpu_info()
    global cpu_arr
    cpu_arr = np.append(cpu_arr, float(cpu_usage))
    if cpu_usage > threshold:
        return str(f"High CPU usage detected: {cpu_usage}%")
    else:
        return [
            str(f"CPU usage : {cpu_usage}% "),
            str(f"CPU model: {cpu_info['brand_raw']} , number of CORS: {cpu_info['count']}, ")]


# Function to check memory usage
def check_memory_usage(threshold=80):
    memory_usage = psutil.virtual_memory().percent
    global ram_arr
    ram_arr = np.append(ram_arr, int(memory_usage))
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
            f"Disk name:{path[0:2]},disk free:{round(disk_usage.free / 1024 ** 3, 2)}  GB ,Disk usage: {disk_usage.percent}% , "
            f"Disk FS type{disk_type}"))
    return ret


# Function to check network traffic
def check_network_traffic(threshold=100 * 1024 * 1024):
    network_traffic = psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent
    network_traffic /= 1024 ** 2 / 8
    global network_arr
    network_arr = np.append(network_arr, int(network_traffic))
    if network_traffic > threshold:
        return str(f"High network traffic detected: {network_traffic} MB")
    else:
        return str(f"network traffic: {network_traffic} MB")


def check_battery():
    battery = psutil.sensors_battery()
    global battery_arr
    battery_arr = np.append(battery_arr, int(battery.percent))
    return str(f"Battery charge:{battery.percent}% , charging:{battery.power_plugged} ")


def get_gpu_temperature():
    gpus = GPUtil.getGPUs()
    gpu = gpus[0]
    return [str(f"GPU model :{gpu.name}"),
            str(f"memory Free:{gpu.memoryFree / 1024} GB , memory usage:{(gpu.memoryUsed / gpu.memoryTotal) * 100}% , GPU temperature: {gpu.temperature}")]


# Function to run health checks
def run_health_checks():

    global bef_time, time_arr
    end_time = time.time()
    time_arr = np.append(time_arr, end_time - bef_time)
    print("Monitoring the system...")
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    gpu = get_gpu_temperature()
    battery = check_battery()
    network = check_network_traffic()
    os.system('cls')
    static = [cpu[1], *check_disk_space(), gpu[0]]
    dynamic = [cpu[0], memory, network, battery, gpu[1]]
    plots = [plot(cpu_arr, time_arr, "CPU", 'time'), plot(ram_arr, time_arr, 'RAM', 'time'),
             plot(network_arr, time_arr, 'network', 'time'), plot(battery_arr, time_arr, 'battery', 'time')]
    return [*static, *dynamic]
