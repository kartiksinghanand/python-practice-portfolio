from typing import List, Dict


# Day 8 - Problem 1
# Topic: Sensor aggregation
#
# Task:
# Given sensor readings, return a dictionary:
# sensor -> average reading
#
# Important:
# - compute average using all readings for the same sensor
# - return averages as floats
# - return {} for empty input
#
# What to return:
# - one dictionary mapping each sensor name to its average value
#
# Expected output for current sample:
# {"temp": 37.0, "hum": 45.0, "dist": 105.0}


readings = [
    {"sensor": "temp", "value": 36.5},
    {"sensor": "hum", "value": 45.0},
    {"sensor": "temp", "value": 37.5},
    {"sensor": "dist", "value": 100.0},
    {"sensor": "dist", "value": 110.0},
]


def average_sensor_values(readings: List[Dict]) -> Dict[str, float]:
    avg_readings: Dict[str, float] = {}
    for reading in readings:
        if reading["sensor"] not in avg_readings:
            avg_readings[reading["sensor"]] = reading["value"]
        else:
            avg_readings[reading["sensor"]] += reading["value"]

    # print("avg_readings: ", avg_readings)
    freq = {}
    for sensor in readings:
        if sensor["sensor"] not in freq:
            freq[sensor["sensor"]] = 1
        else:
            freq[sensor["sensor"]] += 1
    
    sensor_names = avg_readings.keys()
    # print("sensor list:", sensor_names)
    for each_sensor in sensor_names:
        correct_value = avg_readings[each_sensor]/freq[each_sensor]
        avg_readings[each_sensor] = correct_value

    # print(avg_readings)
    # print("freq: ", freq)
    return avg_readings
    
if __name__ == "__main__":
    print(average_sensor_values(readings))
