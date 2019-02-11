# sensors-misc
Misc scripts to read/write various physical sensors

# Sensors
Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor
https://www.adafruit.com/product/4026

This moisture sensor is integrated with Adafruit's Seesaw framework/chip on the PCB.
Which means you interact with Seesaw, not the moisture/temp sensor directly.

adafruit_stemma_soil_sensor_i2c/
* read_native.py
  This provides a native interface to reading values from the sensors on the seesaw chip
* read_library.py
  This provides an example of using Adafruits libraries to read values from the sensors on the seesaw chip
