import psutil


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
def check_disk_space(path='/', threshold=75):
    disk_usage = psutil.disk_usage(path).percent
    if disk_usage > threshold:
        print(f"Low disk space detected: {disk_usage}%")
    else:
        print(f"disk space: {disk_usage}%")


# Function to check network traffic
def check_network_traffic(threshold=100 * 1024 * 1024):
    network_traffic = psutil.net_io_counters().bytes_recv + psutil.net_io_counters().bytes_sent
    if network_traffic > threshold:
        print(f"High network traffic detected: {network_traffic:.2f} MB")
    else:
        print(f"network traffic: {network_traffic:.2f} MB")

def check_cpu_usage(threshold=50):
    cpu_usage = psutil.cpu_percent(interval=1)

    if cpu_usage > threshold:
        print(f"High CPU usage detected: {cpu_usage}%")
    else:
        print(f"CPU usage : {cpu_usage}%")
# Function to run health checks
def run_health_checks():
    print("Monitoring the system...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_space()
    check_network_traffic()
