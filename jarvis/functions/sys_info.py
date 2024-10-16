import psutil
import platform
from typing import List

def get_system_info():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)

    # Get RAM usage
    memory = psutil.virtual_memory()
    total_ram = memory.total / (1024 ** 3)  # Convert to GB
    used_ram = memory.used / (1024 ** 3)    # Convert to GB
    ram_usage_percent = memory.percent

    # Get battery information
    battery_info = psutil.sensors_battery()
    battery_percent = battery_info.percent if battery_info else "No battery detected"
    power_plugged = battery_info.power_plugged if battery_info else False

    # Get OS information
    os_info = platform.system()

    # Print the results
    print(f"Operating System: {os_info}")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Total RAM: {total_ram:.2f} GB")
    print(f"Used RAM: {used_ram:.2f} GB ({ram_usage_percent}%)")
    if battery_info:
        print(f"Battery Percentage: {round(battery_percent, 2)}%")
        print(f"Power Plugged: {'Yes' if power_plugged else 'No'}")
        return f"The Operating System you are using is {os_info}. The CPU usage is at {cpu_usage} percent. The total RAM is {total_ram:.2f} gigabytes. The used RAM is {used_ram:.2f} gigabytes. The battery percentage is at {battery_percent:.2f}percent. The power is " + ('plugged' if power_plugged else 'not plugged') + "."
    else:
        return "No battery information available."

def get_battery_info():
    battery_info = psutil.sensors_battery()
    battery_percent = battery_info.percent if battery_info else "No battery detected"
    power_plugged = battery_info.power_plugged if battery_info else False

    return round(battery_percent, 2), power_plugged

def get_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

def get_ram_usage():
    memory = psutil.virtual_memory()
    total_ram = memory.total / (1024 ** 3)  # Convert to GB
    used_ram = memory.used / (1024 ** 3)    # Convert to GB
    ram_usage_percent = memory.percent

    return total_ram, used_ram, ram_usage_percent

def get_os_info():
    os_info = platform.system()
    return os_info

def chech_system_info(prompt):
    if "get system info" in prompt.lower():
        system_info = get_system_info()
        return True, system_info
    elif "get battery info" in prompt.lower():
        battery_info = get_battery_info()
        print(f"Battery Percentage: {battery_info[0]}%")
        print(f"Power Plugged: {'Yes' if battery_info[1] else 'No'}")
        result = "The battery percentage is at " + str(battery_info[0]) + " percent. The power is " + ('plugged' if battery_info[1] else 'not plugged') + "."
        return True, result
    elif "get cpu usage" in prompt.lower():
        cpu_usage = get_cpu_usage()
        print(f"CPU Usage: {cpu_usage}%")
        result = "The CPU usage is at " + str(cpu_usage) + " percent."
        return True, result
    elif "get ram usage" in prompt.lower():
        ram_usage = get_ram_usage()
        print(f"Total RAM: {ram_usage[0]:.2f} GB")
        print(f"Used RAM: {ram_usage[1]:.2f} GB ({ram_usage[2]}%)")
        result = "The total RAM is " + str(ram_usage[0]) + " gigabytes. The used RAM is " + str(ram_usage[1]) + " gigabytes."
        return True, result
    
    elif "get os info" in prompt.lower():
        os_info = get_os_info()
        print(f"Operating System: {os_info}")
        result = "The Operating System you are using is " + os_info + "."
        return True, result
    else:
        return False, ""
    

# test the function
if __name__ == "__main__":
    print(get_system_info())
    print(get_battery_info())
    print(get_cpu_usage())
    print(get_ram_usage())