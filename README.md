# ROV Prototype Repo
## University of Ottawa Engineering students working towards making a prototype ROV

### How to use:
Dev: here goes whatever code you're immediately working on

Production: here goes whatever code you're trying to implement into the main group

Release: here goes the current "can go on the ROV" code, reserved for feature and stability updates


# Setup Instructions 
Written in part by:
- Stefan T
- Sebastian L
### Important Information
- This project is built around Raspbian Lite, and expects a fresh install
- To prepare it, download the latest build of Raspbian Lite and burn it to an SD card using software such as Etcher
- Also ensure that the Raspberry Pi and your computer are connected to the same network and they have a functional WAN connection during the setup process
- A router is currently required during offsite testing to handel communication between the ROV Raspberry Pi and the control laptop



## Setup Instructions on Raspberry Pi
1. sudo raspi-config
    1. System Options > Hostname > ROVPI
    2. Interface Options > SSH > Enable
    3. Interface Options > Remote GPIO > Enable
    4. Performance Options > Overclock > Modest
    5. Performance Options > GPU Memory > 16
    6. Advanced Options > Expand File System > YES
    7. Finish
    8. Reboot now
 1. passwd
    1. Set password to "ROV2021"
 2. sudo apt-get update && sudo apt-get upgrade
 3. sudo apt-get install motion python3-pip python3-gpiozero pigpiod dht11
 4. lsusb
    1. Ensure the camera is listed
 5. sudo nano /etc/motion/motion.conf 
    1. Set 'daemon' to ON
    2. Set 'framerate' to 15
    3. Set 'Stream_port' to 8081
    4. Set 'Stream_quality' to 50
    5. Set 'Stream_localhost' to OFF
    6. Set 'webcontrol_localhost' to OFF
    7. Set 'quality' to 50
    8. Set 'width' & 'height' to 320 & 240
    9. Set 'stream_maxrate' to 30
    10. Set 'start_motion_daemon' to yes
    11. Save and exit ( ctr + x)
    12. sudo service motion restart
    13. sudo motion
 6.  wget "https://raw.githubusercontent.com/KelpieRobotics/prototype/release/rov.py"

## Setup Instructions on Laptop
1. SSH into the raspberry pi using the computer for example 'ssh pi@192.168.40.149' with '192.168.40.149' being the pi's ip address which can be found on the router's web interface
2. Type in the password 'ROV2021' when requested 
3. Type 'python3 rov.py' to start the motion control software
4. Open a webbroswer and navigate to 'http://192.168.40.149:8081' again with '192.168.40.149' being the pi's ip address to view the camera
5. You can now return to the SSH session to control the ROV



### Credits for Video Feed Instructions
The following guide was adapted: 
[How to Make Raspberry Pi Webcam Server and Stream Live Video](https://www.instructables.com/How-to-Make-Raspberry-Pi-Webcam-Server-and-Stream-/)


Along with a comment from pelodark

Written in part by:
Stefan T
Sebastian L
