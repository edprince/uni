#Hardware report for Lego Robot Game ALL Project#
##Components##
The EV3 brick makes use of a micro USB port, enabling it to be connected to a
computer, and sync code created in the Mindstorms software. This has a speed of
480 Mbit/s. It uses USB 2.0 to communicate with a computer, as well as USB 1.1 for
connecting to other EV3 bricks (daisy chaining) (Xander Soldaat 2013). The brick communicates to
a large and a medium motor, with 160 - 170 RPM and 240- 250 RPM respectively
(Xander Soldaat 2013)

##Processing##
The main brick makes use of a 300MHz ARM9
processor. The robot operates on a
Linux-based operating system (Laurens Valk 2013).

##Memory##
The brick also contains an Micro SD-Card
Reader, that can handle up to 32GB, along with 16MB of flash memory, and 64MB of
RAM (Xander Soldaat 2013). This quantity of memory has allowed us to store the
programs on the brick itself, and use variables within the program, which are
stored in the bricks memory.

##Sensors##
###Infrared###
The robot makes use of the infra-red sensor, an optical sensor, a touch sensor,
motors and the core EV3 brick. 
The infrared sensor can read signals at a proximity between 50cm and 70cm away.
It also supports 4 signal channels to avoid signal confusion. (The LEGO Group
2015). We were able to use this to detect obstacles throughout the maze, and
detect the positions of the deposit boxes at the end of the game.

###Optical Sensor###
The optical sensor can distinguish 7 different colours, as well as a lack of a
colour, giving the programmer many options. (Xander Soldaat 2013). We used the 
sensor multiple times throughout the game, for line following purposes, the 
maze-solving algorithm, to signal when to begin the mini-game, finishing the 
maze and deciding whether or not the deposit location is correct for the placing 
of the object to finish the game. We found that a limitation of the sensor was 
that it sometimes had difficulty registering certain colours, in particular 
green, yellow and white, with which it often registered as a different colour.

###Touch Sensor###
We used the touch sensor for a very simple purpose, which was starting the game.
The program would be halted at the start until the player activates the touch
sensor, indicating that the robot should begin.

##References##
Xander Soldaat 2013 *Comparing the NXT and EV3 Bricks* [online] available from
<http://botbench.com/blog/2013/01/08/comparing-the-nxt-and-ev3-bricks> [8 January
2013]  
Laurens Valk 2013 *LEGO MINDSTORMS EV3 - A new Generation!* [online] available
from <http://robotsquare.com/2013/01/07/lego-mindstorms-ev3-new-generation> [7 January
2013]  
The LEGO Group 2015 *EV3 Infrared Sensor* [online] available from
<https://shop.education.lego.com/legoed/en-US/catalog/product.jsp?productId=45509&ProductLine=LEGO-MINDSTORMS-Education-EV3> [2015]



#Bluetooth#
The EV3 brick uses Bluetooth version 2.1+EDR (Xander Soldaat 2013), allowing the
data transfer to occur at 24Mbit/s, proving to be 2 - 3 times faster than the
previous version of Bluetooth (Maragret Rouse 2010). The Bluetooth support meant
that we were capable of connecting an Android-powered mobile device to the
brick, and send data, using the 'EV3 Mailbox Remote' application. Within our game, we have
taken advantage of the Bluetooth capabilities twice. The first was to receive an
answer from a phone (to a mathematical question put to the player). Then the
robot can delegate a bonus accordingly. The second use is for the user to send a
message the robot to inform which layout they have decided to use at the end of
the maze. 

Maragret Rouse 2010 *Bluetooth 2.0+EDR* [online] available from
<http://whatis.techtarget.com/definition/Bluetooth-20EDR> [2010]
