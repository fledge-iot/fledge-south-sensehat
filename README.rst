foglamp-south-sensehat
========================

South Plugin for Raspberry PI Sense HAT

This directory contains a plugin that pulls readings from Sensor HAT.
The Sense HAT features an 8x8 RGB LED matrix, a mini joystick and the following sensors:

- Gyroscope
- Accelerometer
- Magnetometer
- Temperature
- Humidity
- Barometric pressure

The polling is done at fixed intervals which is configurable via "pollInterval" configuration item.

All sensors can be enabled/disabled separately vide setting suitable configuration parameters. All sensors can also be named as desired vide setting suitable configuration parameters.

Installing the software:
========================

It is always recommended using the most up-to-date version of Raspbian, and it often helps to start with a completely fresh install of Raspbian, although this isn't necessary.

The plugin can be installed with given `requirements.sh <requirements.sh>`_ or the following steps:

::

           sudo apt install -y sense-hat

Once that's done, it's probably a good idea to reboot your Pi to let the changes propagate.
