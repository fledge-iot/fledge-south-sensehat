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


Also it is required to enable I2C on the RPi, please do the following steps:
1) sudo raspi-config
2) Choose Interfacing options
3) Choose P5I2C option Enable/Disable automatic loading of I2C Kernel module
4) Follow the prompt to set Yes for ARM I2C interface enabled
5) Once that's done, reboot your RPi to let the changes propagate.
6) And with below command be ensure that your I2C is enabled

::

            ls /dev/*i2c*

For more help, please visit https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

Or a simple alternative approach to enable I2C is:

1) Download script via wget https://get.pimoroni.com/i2c
2) sudo bash i2c
3) sudo reboot
