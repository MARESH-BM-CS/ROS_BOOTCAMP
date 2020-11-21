#!/usr/bin/env python 

# Header files
import rospy 
from std_msgs.msg import Float32

def publisher(): #defining a function called publisher, it takes no arguements  
    pub_node = rospy.Publisher('float_incrementer', Float32, queue_size = 10) #variable pub_node publishes to a topic called '/float_incrementer' whose message type is float
    rospy.init_node('publisher', anonymous = True) #initializes a node and gives it a unique identity
    rate = rospy.Rate(5) # 5 Hz 
    msg_to_pub=0
    while not rospy.is_shutdown():
        msg_to_pub+=1 #variable called msg_to_pub will contain the contents of the message 
        pub_node.publish(msg_to_pub) #sending out the message content which is float value
        rospy.sleep(5) #wait 5s

if __name__ == '__main__':
    try: 
        publisher() 

    except rospy.ROSInterruptException:
        pass
