# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time
import psutil
from check import run_health_checks

def print_hi():
    for process in psutil.process_iter(['pid', 'name', 'memory_info', 'cpu_percent']):
        print(process.info)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi()
    while True:
        os.system('cls')
        run_health_checks()
        time.sleep(5)  # pause for 5 seconds


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
