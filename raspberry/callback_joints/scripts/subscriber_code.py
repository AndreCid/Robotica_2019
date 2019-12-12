#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState

def callback(msg):
    print(msg.position)

rospy.init_node('topic_subscriber')
sub = rospy.Subscriber('joint_states', JointState, callback)
rospy.spin()
