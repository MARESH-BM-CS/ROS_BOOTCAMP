#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float32

def xyz(received_data): 
    rospy.loginfo(rospy.get_caller_id() + '%f', received_data.data) #callback function that gets the data 

def subscriber(): 
    rospy.init_node('subscriber', anonymous = True) #initializes a node 
    sub_node=rospy.Subscriber('float_incrementer', Float32, xyz) #subscribes to a topic called '/float_incrementer'
    rospy.spin() #run until user stops 

if __name__ == '__main__':
    subscriber()
    rospy.sleep(1) #wait for 1s