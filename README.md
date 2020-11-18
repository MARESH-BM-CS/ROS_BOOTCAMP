# ROS_BOOTCAMP
This Repository includes introduction to ROS and its basic terminologies

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

