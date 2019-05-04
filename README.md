# Microbit Light Installation
A Light Installation that uses multiple BBC Microbits

In order to make this light installation you need to set up one Microbit that functions as as the beacon and sends a signal on a specific radio strength. At least one other Microbit is needed that functions as the receiver and will show the distance to the beacon with an LED light.

All code for this installation is written in MicroPython.

Instructions for the Beacon:
Connect the pulse sensor and the Neopixel ring to the Microbit (see [beacon_schematic.png](https://github.com/vkostova/Microbit-Light-Installation/blob/master/beacon_schematic.png)).
After the physical installation push the code [beacon.py](https://github.com/vkostova/Microbit-Light-Installation/blob/master/Beacon.py) onto the Microbit.
The pulse sensor should now be reading a users pulse when it is being touched and the Neopixel ring will light up in response to the readings from the pulse sensor.

Instructions for the Receiver:
Connect the RGB LED light to the Microbit (see [receiver_schematic.png](https://github.com/vkostova/Microbit-Light-Installation/blob/master/receiver_schematic.png)).
After the physical installation push the code [receiver.py](https://github.com/vkostova/Microbit-Light-Installation) onto the Microbit.
The light will now light up and show the distance to the beacon by changing their color.
As many receiver lights can be installed as wanted.
