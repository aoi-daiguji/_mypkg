#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 Daiguji Aoi
# SPDX-License-Identifier; BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16 

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0

def cd():
    global n
    msg = Int16()
#    msg.name = "大宮司葵生" 
    msg.data = n
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cd)
rclpy.spin(node)
