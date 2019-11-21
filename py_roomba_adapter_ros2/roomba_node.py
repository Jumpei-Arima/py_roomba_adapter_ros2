#!/usr/bin/env python
#! coding: utf-8

import os

import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from std_msgs.msg import String
from geometry_msgs.msg import Twist

from pyroombaadapter import PyRoombaAdapter

class RoombaNode(Node):
    def __init__(self):
        print('Roomba node!')
        super().__init__('roomba_node')
        
        PORT = "/dev/ttyUSB0"
        self.adapter = PyRoombaAdapter(PORT)
        self.twist_sub = self.create_subscription(Twist, "/cmd_vel", self.twist_callback)

    def twist_callback(self, msg):
        print('callback')
        velocity = msg.linear.x
        yaw_rate = msg.angular.z
        self.adapter.move(velocity, yaw_rate)

def main(args=None):
    rclpy.init(args=args)

    node = RoombaNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
