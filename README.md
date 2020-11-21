# ROS_BOOTCAMP
This Repository includes introduction to ROS,its basic terminologies,few basic commands,few concepts in ROS,turtlebot in gazebo(3D simulator for robot)

**a) what is  ROS? its advantages? its limitations?**

***ROS*** is a easy-to-use framework for writing robot software. It is a set of software libraries and tools used to simplify the task of creating complex and robust robot functions across a variety of robotic platforms. It is an open-source,meta-operating system for a robot.

***Advantages***:

------------------

*ROS provides important robot-specific capabilities such as navigation,mapping,diagnostics,localization,pose estimation,preemptable remote procedure calls,robot geometry library,standard message definitions for robots,robot description language.

*ROS tools support introspecting, debugging, plotting, and visualizing the state of the system bbeing developed. rviz and rqt provide graphical tools functionality.

*Improved encapsulation of communication systems/message passing systems and code reuse.

*ROS is an open source and include seamless integration features with third party environments.

*ROS has large community of users worldwide which offers collaborative environment among users and world class roboticists

*Runs on on multi language like Python,CPP,Octave...etc.

***limitations***:

------------------

*Powerful hardware required to run ROS on Robot.

*Not useful in developing novel applications where reusing of packages is not preferred,and thus requires lots of time-consuming modifications.

*Since ROS must support a large range of topologies and frameworks, messages sent via ROS are often duplicated taking up more bandwidth than necessary.

*Not a real-time system (inherent latency in processes).

*Security issues for industrial deployment scenarios.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**b) Basic terminologies in ROS:**

-----------------------------------

*WORKSPACE*: Spaces where we can modify, build existing packages or install new packages. Workspace  can contain up to four different spaces which each serve a different 	role in the software development process,such as source space,build space,development space,install space,result space.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*ROS PACKAGE*: It is the main organizational software which contains ROS nodes,ROS-independent library,dataset,configuration files etc.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*NODES*: processes which performs computation.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*MESSAGES*: They are data-structures such as int ,float,boolean etc. Communication of one node to another node involves message passing.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*TOPICS*: Channels through which messages are passed. It is the name given to identify the contents of the messages being passed.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*SERVICES*: Avails request/reply interactions in distributed systems 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
***Publisher Node and Subscriber Nodes***:

----------------------------------------------------------

*Publisher Node publish or sends messages of any datatype to subscriber Node through a specific topic. 

*Subscriber node requests a connection to publisher through the same specific topic and a list of protocols. The subscriber then establishes a *separate* connection when The publisher  selects a protocol from that list.

-------------------------------------------------------------------------------------------------------------------------------------------

***Few Basic Commands*** :

----------------------------------------------------------------------------------------------------------------------------------------------

*roscore* : 
    will start up a ROS Master,a ROS parameter server and  rosout

*rosrun*: 
    rosrun can be used to run a executable in a specified package 

*rostopic list*: 
    it is used to to display topic's runtime information

*rostopic echo*:
    it is used to display topic related info

*rosmsg show*: 
    
    it is used to check message transmitted and also to display the fields in a ROS massage
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
***Some concepts in ROS:***

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

**ROS navigation stack*:

It takes data stored in odometry and sensors streams and sends to the moving base of the bot. Then the bot is able to know path in its environment automatically from one point to another.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Localization and sensors used in Localization*: 

Localization is the process of estimating the position of the robot with respect to its environment.
Robot localization in ROS is done using AMCL(Adaptive Monte-Carlo Localization) in 3D it uses radio-range sensors and laser sensors

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**mapping*: 

It is the process of designing the robot's environment using sensors data like obstacles and path 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**tf in ROS and its use*:

*tf in ROS is a package which keeps track of multiple 3D coordinate frames over time. 

*tf is used to recieve and buffer all coordinate frames that are broadcasted in the system and can be used later to send out the relative pose of coordinate frames to the rest of the system.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**SLAM problem*:

*SLAM ->Simultaneous Mapping And Localization 

*SLAM problem is like a chicken-or-egg problem: 

-> a map is needed for localization and 

->a pose estimate is needed for mapping 

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
***Experiments on turtlebot robot in gazebo***:
------------------------------------------------

*spawned turtlebot robot in gazebo

*sensors info:

1).odometry:

​				topic name: /odom

​				publisher:*/gazebo(http://rosdscomputer:39789/)

​				subscriber: None

​				message Type: nav_msgs/Odometry

2).Kobuki Laser Scan Data(LIDAR):


​				topic name: /kobuki/laser/scan 

​				publisher: * /gazebo (http://rosdscomputer:39789/)

​				subscriber: None

​				message Type: sensor_msgs/LaserScan

3).RGB Camera info:

​				topic name: /camera/rgb/camera_info

​				publisher: * /gazebo (http://rosdscomputer:39789/)

​				subscriber: None

​				message Type: sensor_msgs/CameraInfo




