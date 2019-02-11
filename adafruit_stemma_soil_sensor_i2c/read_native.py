#!/usr/bin/env python3

import time
import struct
from smbus2 import SMBusWrapper, i2c_msg

device = {
    "address": 0x36,
    "sleep": 0.05,
    "sensors": {
        "moisture": {
            "register": [0x0F, 0x10],
            "bytes": 2,
            "format": ">H",
        },
        "temperature": {
            "register": [0x00, 0x04],
            "bytes": 4,
            "format": ">I",
            "modifier": lambda x: round(0.00001525878 * x, 2)
        }
    }
}


def read_sensor(address, details):
    # Send our target register to load
    msg = i2c_msg.write(address, details["register"])
    bus.i2c_rdwr(msg)

    # Wait for the device to load the values
    time.sleep(device["sleep"])

    # Read the target register values
    msg = i2c_msg.read(address, details["bytes"])
    bus.i2c_rdwr(msg)

    # Turn the response into our target format
    buf = bytearray(list(msg))
    ret = struct.unpack(details["format"], buf)[0]

    if "modifier" in details:
        ret = details["modifier"](ret)

    return ret


with SMBusWrapper(1) as bus:
    while True:
        for sensor, details in device["sensors"].items():
            value = read_sensor(device["address"], details)

            print("{0}: {1}".format(sensor, value))
            time.sleep(1)
