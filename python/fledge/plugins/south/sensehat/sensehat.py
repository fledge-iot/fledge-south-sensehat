# -*- coding: utf-8 -*-

# FLEDGE_BEGIN
# See: http://fledge.readthedocs.io/
# FLEDGE_END

""" Module for Sense HAT 'poll' type plugin """

import copy
import logging

from sense_hat import SenseHat

from fledge.common import logger
from fledge.plugins.common import utils


__author__ = "Ashish Jabble"
__copyright__ = "Copyright (c) 2018 Dianomic Systems"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"


_DEFAULT_CONFIG = {
    'plugin': {
        'description': 'Sense HAT Poll Plugin',
        'type': 'string',
        'default': 'sensehat',
        'readonly': 'true'
    },
    'assetNamePrefix': {
        'description': 'Prefix of asset name',
        'type': 'string',
        'default': 'sensehat/',
        'order': '2',
        'displayName': 'Asset Name Prefix'
    },
    'pressureSensor': {
        'description': 'Enable Barometric Pressure sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '3',
        'displayName': 'Pressure Sensor'
    },
    'pressureSensorName': {
        'description': 'Asset name of Barometric Pressure sensor',
        'type': 'string',
        'default': 'pressure',
        'order': '4',
        'displayName': 'Pressure Sensor Name'
    },
    'temperatureSensor': {
        'description': 'Enable Temperature sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '5',
        'displayName': 'Temperature Sensor'
    },
    'temperatureSensorName': {
        'description': 'Asset name of Temperature sensor',
        'type': 'string',
        'default': 'temperature',
        'order': '6',
        'displayName': 'Temperature Sensor Name'
    },
    'humiditySensor': {
        'description': 'Enable Humidity sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '7',
        'displayName': 'Humidity Sensor'
    },
    'humiditySensorName': {
        'description': 'Asset name of Humidity sensor',
        'type': 'string',
        'default': 'humidity',
        'order': '8',
        'displayName': 'Humidity Sensor Name'
    },
    'gyroscopeSensor': {
        'description': 'Enable IMU (inertial measurement unit) gyroscope sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '9',
        'displayName': 'Gyroscope Sensor'
    },
    'gyroscopeSensorName': {
        'description': 'Asset name of Gyroscope sensor',
        'type': 'string',
        'default': 'gyroscope',
        'order': '10',
        'displayName': 'Gyroscope Sensor Name'
    },
    'accelerometerSensor': {
        'description': 'Enable IMU (inertial measurement unit) accelerometer sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '11',
        'displayName': 'Accelerometer Sensor'
    },
    'accelerometerSensorName': {
        'description': 'Asset name of accelerometer sensor',
        'type': 'string',
        'default': 'accelerometer',
        'order': '12',
        'displayName': 'Accelerometer Sensor Name'
    },
    'magnetometerSensor': {
        'description': 'Enable IMU (inertial measurement unit) magnetometer/compass sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '13',
        'displayName': 'Magnetometer Sensor'
    },
    'magnetometerSensorName': {
        'description': 'Asset name of magnetometer sensor',
        'type': 'string',
        'default': 'magnetometer',
        'order': '14',
        'displayName': 'Magnetometer Sensor Name'
    },
    'joystickSensor': {
        'description': 'Enable Joystick sensor',
        'type': 'boolean',
        'default': 'true',
        'order': '15',
        'displayName': 'Joystick Sensor'
    },
    'joystickSensorName': {
        'description': 'Asset name of Joystick sensor',
        'type': 'string',
        'default': 'joystick',
        'order': '16',
        'displayName': 'Joystick Sensor Name'
    }
}

_LOGGER = logger.setup(__name__, level=logging.INFO)
sense = SenseHat()


def plugin_info():
    """ Returns information about the plugin.

    Args:
    Returns:
        dict: plugin information
    Raises:
    """

    return {
        'name': 'Sense HAT Poll Plugin',
        'version': '1.9.1',
        'mode': 'poll',
        'type': 'south',
        'interface': '1.0',
        'config': _DEFAULT_CONFIG
    }


def plugin_init(config):
    """ Initialise the plugin.

    Args:
        config: JSON configuration document for the South plugin configuration category
    Returns:
        handle: JSON object to be used in future calls to the plugin
    Raises:
    """
    data = copy.deepcopy(config)
    return data


def plugin_poll(handle):
    """ Extracts data from the sensor and returns it in a JSON document as a Python dict.

    Available for poll mode only.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:
        returns a sensor reading in a JSON document, as a Python dict, if it is available
        None - If no reading is available
    Raises:
        Exception
    """
    def _str_to_bool(s):
        return True if s == 'true' else False

    # The IMU (inertial measurement unit) sensor is a combination of three sensors, each with an x, y and z axis
    # Enables and disables the magnetometer, accelerometer, gyroscope
    sense.set_imu_config(_str_to_bool(handle['magnetometerSensor']['value']),
                         _str_to_bool(handle['gyroscopeSensor']['value']),
                         _str_to_bool(handle['accelerometerSensor']['value']))
    time_stamp = utils.local_timestamp()
    data = list()
    asset_prefix = handle['assetNamePrefix']['value']
    try:
        if handle['pressureSensor']['value'] == 'true':
            pressure = sense.get_pressure()
            data.append({
                'asset': '{}{}'.format(asset_prefix, handle['pressureSensorName']['value']),
                'timestamp': time_stamp,
                'readings': {"pressure": pressure}
            })
        if handle['temperatureSensor']['value'] == 'true':
            temperature = sense.get_temperature()
            data.append({
                'asset': '{}{}'.format(asset_prefix, handle['temperatureSensorName']['value']),
                'timestamp': time_stamp,
                'readings': {"temperature": temperature}
            })
        if handle['humiditySensor']['value'] == 'true':
            humidity = sense.get_humidity()
            data.append({
                'asset': '{}{}'.format(asset_prefix, handle['humiditySensorName']['value']),
                'timestamp': time_stamp,
                'readings': {"humidity": humidity}
            })
        if handle['magnetometerSensor']['value'] == 'true':
            magnetometer = sense.get_compass_raw()
            data.append({
                'asset': '{}{}'.format(asset_prefix, handle['magnetometerSensorName']['value']),
                'timestamp': time_stamp,
                'readings': magnetometer
            })
        if handle['gyroscopeSensor']['value'] == 'true':
            gyroscope = sense.get_gyroscope_raw()
            data.append({
                'asset': '{}{}'.format(asset_prefix, handle['gyroscopeSensorName']['value']),
                'timestamp': time_stamp,
                'readings': gyroscope
            })
        if handle['accelerometerSensor']['value'] == 'true':
            accelerometer = sense.get_accelerometer_raw()
            data.append({
                'asset': '{}{}'.format(asset_prefix, handle['accelerometerSensorName']['value']),
                'timestamp': time_stamp,
                'readings': accelerometer
            })
        if handle['joystickSensor']['value'] == 'true':
            for event in sense.stick.get_events():
                data.append({
                    'asset': '{}{}'.format(asset_prefix, handle['joystickSensorName']['value']),
                    'timestamp': time_stamp,
                    'readings': {"direction": event.direction, "action": event.action}
                })
    except RuntimeError as e:
        _LOGGER.exception("Sense HAT runtime error: %s", e)
        raise e
    except Exception as ex:
        _LOGGER.exception("Sense HAT exception: %s", ex)
        raise ex
    else:
        return data


def plugin_reconfigure(handle, new_config):
    """  Reconfigures the plugin

    it should be called when the configuration of the plugin is changed during the operation of the South plugin service;
    The new configuration category should be passed.

    Args:
        handle: handle returned by the plugin initialisation call
        new_config: JSON object representing the new configuration category for the category
    Returns:
        new_handle: new handle to be used in the future calls
    """
    _LOGGER.info("Old config for Sense HAT plugin {} \n new config {}".format(handle, new_config))

    new_handle = copy.deepcopy(new_config)
    return new_handle


def plugin_shutdown(handle):
    """ Shutdown the plugin doing required cleanup, to be called prior to the South plugin service being shut down.

    Args:
        handle: handle returned by the plugin initialisation call
    Returns:

    """
    _LOGGER.info('Sense HAT poll plugin shut down.')
