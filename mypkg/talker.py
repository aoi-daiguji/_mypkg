import rclpy
from rclpy.node import Node
from person_msgs.msg import Person 

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0

def cd():
    global n
    msg = Person()
    msg.name = "大宮司葵生" 
    msg.age = n
    pub.publish(msg)
    n += 1

node.create_timer(0.5, cd)
rclpy.spin(node)
