from typing import List, Dict


# Day 7 - Problem 2
# Topic: Filtering + ordering
#
# Task:
# Given a list of devices, return the names of devices that are:
# - active == True
# - battery >= 30
#
# Return names sorted by battery descending.
# If two devices have the same battery, sort names alphabetically.
#
# What to return:
# - only the device names, not tuples or dictionaries
#
# Expected output for current sample:
# ["sensor_a", "sensor_e", "sensor_d"]


devices = [
    {"name": "sensor_a", "battery": 90, "active": True},
    {"name": "sensor_b", "battery": 20, "active": True},
    {"name": "sensor_c", "battery": 55, "active": False},
    {"name": "sensor_d", "battery": 55, "active": True},
    {"name": "sensor_e", "battery": 75, "active": True},
]


def healthy_devices(devices: List[Dict]) -> List[str]:
    active_devices = []
    for device in devices:
        if device["active"] == True and device["battery"] >= 30:
            active_devices.append((device["name"], device["battery"]))
    active_devices_sorted = sorted(active_devices, key = lambda k: (-k[1],k[0]))
    return [sensor [0] for sensor in active_devices_sorted]

if __name__ == "__main__":
    print(healthy_devices(devices))
