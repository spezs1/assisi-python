#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Python interface to simulated bees. """

import threading
import time

import zmq

from msg import dev_msgs_pb2
from msg import base_msgs_pb2


LENGTH = 2
""" Bee length, in centimetres. """

WIDTH = 0.8
""" Bee width, in centimetres. """

WHEEL_DISTANCE = 0.4
""" Axle width of the underlying differential-wheeled model. """

# Device ID definitions (for convenience)
""" IR range sensors """

IR_SIDE_RIGHT = 0 #: Sensor at 90°
""" Right range sensor """

IR_RIGHT_FRONT = 1
""" Right-front range sensor """

IR_FRONT = 2
""" Front range sensor """

IR_LEFT_FRONT = 3
""" Left-front range sensor """

IR_SIDE_LEFT = 4
""" Left range sensor """

LIGHT_SENSOR = 5
""" Light sensor """


TEMP_SENSOR = 6
""" Temperature sensor """

class Bee:
    """ 
    The low-level interface to Bee 'robots'. 
    This clas provides an api for programming bee behaviors.
    It creates a connection to the data source, i.e., the simulated bee.
    Waits for the bee of specified by 'name' to be spawned into the simulator.

    :param string rtc_file_name: Name of the run-time-configuration (RTC) file. This file specifies the simulation connection parameters and the name of the simulated bee object.
    :param string name: The name of the bee (if not specified in the RTC file).
    """
    
    def __init__(self, rtc_file_name='', name = 'Bee'):
        
        
        if rtc_file_name:
            # Parse the rtc file
            pass
        else:
            # Use default values
            self.__pub_addr = 'tcp://127.0.0.1:5556'
            self.__sub_addr = 'tcp://127.0.0.1:5555'
            self.__name = name
            self.__ir_range_readings = dev_msgs_pb2.RangeArray()
            self.__encoder_readings = dev_msgs_pb2.DiffDrive()
            self.__true_pose = base_msgs_pb2.PoseStamped()
            self.__light_readings = base_msgs_pb2.ColorStamped()
            self.__temp_readings = dev_msgs_pb2.TemperatureArray()

            # Create the data update thread
            self.__connected = False
            self.__context = zmq.Context(1)
            self.__comm_thread = threading.Thread(target=self.__update_readings)
            self.__comm_thread.daemon = True
            self.__lock =threading.Lock()
            self.__comm_thread.start()

            # Connect the publisher socket
            self.__pub = self.__context.socket(zmq.PUB)
            self.__pub.connect(self.__pub_addr)

            # Wait for the connection
            while not self.__connected:
                pass
            print('{0} connected!'.format(self.__name))

            # Wait one more second to get all the data
            time.sleep(0.5)

    def __update_readings(self):
        """ 
        Get a message from Bee and update data. 
        """
        self.__sub = self.__context.socket(zmq.SUB)
        self.__sub.connect(self.__sub_addr)
        #self.__sub.setsockopt(zmq.HWM, 1)
        self.__sub.setsockopt(zmq.SUBSCRIBE, self.__name)
                    
        while True:
            [name, dev, cmd, data] = self.__sub.recv_multipart()
            self.__connected = True
            
            ### Range readings ###
            if dev == 'IR':
                if cmd == 'Ranges':
                    # Protect write with a lock
                    # to make sure all data is written before access
                    with self.__lock:
                        self.__ir_range_readings.ParseFromString(data)
                else:
                    print('Unknown command {0} for {1}'.format(cmd, self.__name))

            ### Base data ###
            elif dev == 'Base':
                if cmd == 'Enc':
                    with self.__lock:
                        self.__encoder_readings.ParseFromString(data)
                elif cmd == 'GroundTruth':
                    with self.__lock:
                        self.__true_pose.ParseFromString(data)
                else:
                    print('Unknown command {0} for Bee {1}'.format(cmd, self.__name))
            ### Light sensors ###
            elif dev == 'Light':
                if cmd == 'Readings':
                    with self.__lock:
                        self.__light_readings.ParseFromString(data)
                else:
                    print('Unknown command {0} for Bee {1}'.format(cmd, self.__name))

            ### Temperature sensors ###
            elif dev == 'Temp':
                if cmd == 'Temperatures':
                    with self.__lock:
                        self.__temp_readings.ParseFromString(data)
                else:
                    print('Unknown command {0} for Bee {1}'.format(cmd, self.__name))

            else:
                print('Unknown device {0} for Bee {1}'.format(dev, self.__name))


    def get_range(self, id):
        """ 
        Returns the range reading corresponding to sensor id. 
        
        TODO: Fix the hacky correction of invalid readings
        """
        with self.__lock:
            range = self.__ir_range_readings.range[id]

        # Hack to fix error of range 0.0 appearing
        # when no obstacles are present
        if range < 0.000001:
            range = 10

        return range

    def get_temp(self, id = TEMP_SENSOR):
        """
        Returns the temperature reading of sensor id.
        """
        with self.__lock:
            return self.__temp_readings.temp[id - TEMP_SENSOR]
        

    def get_vibration_frequency(self, id):
        """
        Returns the vibration frequency of sensor id.
        """
        pass

    def get_vibration_amplitude(self, id):
        """
        Returns the vibration amplitude of sensor id.
        """
        pass

    def get_light_rgb(self, id = LIGHT_SENSOR):
        """
        :return: (r,g,b) tuple, representing the light intensities at
                 red, green and blue wavelengths (currently, the sensor
                 reports only blue intensity, r and g are always 0).
        """
        with self.__lock:
            return (self.__light_readings.color.red,
                    self.__light_readings.color.green,
                    self.__light_readings.color.blue)

    def get_true_pose(self):
        """ 
        :return: (x,y,yaw) tuple, representing te true pose of the bee
                 in the world.
        """
        with self.__lock:
            return (self.__true_pose.pose.position.x,
                    self.__true_pose.pose.position.y,
                    self.__true_pose.pose.orientation.z)
    
    def set_vel(self, vel_left, vel_right):
        """ 
        Set wheel velocities. 

        Bee body velocities depend on wheel velocities in the following way:
        
        .. math:: v = \\frac{v_{left}+v_{right}}{2}
        .. math:: \\omega = \\frac{v_{right}-v_{left}}{d}

        where d is the distance between the wheels ("axle length").

        :param float vel_left: Left wheel velocity.
        :param float vel_right: Right wheel velocity.
        """
        vel = dev_msgs_pb2.DiffDrive();
        vel.vel_left = vel_left
        vel.vel_right = vel_right
        self.__pub.send_multipart([self.__name, "Base", "Vel", 
                                   vel.SerializeToString()])

if __name__ == '__main__':
    
    bee1 = Bee(name = 'Bee')
    bee1.set_vel(5, 5)
    while True:
        for i in range(8):
            print('{0} '.format(bee1.get_range(i)))

