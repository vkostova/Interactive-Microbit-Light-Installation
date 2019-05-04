from microbit import *
import radio
radio.on()

def set_rgb(green, red, blue):
    pin0.write_analog(green)
    pin1.write_analog(red)
    pin2.write_analog(blue)

# receiver will show the distance to the beacon
# the number of receivers should be easily adjustable
while True:
    message = radio.receive_full()
    incoming = radio.receive()
    if message:
        strength = message[1]+100
        displaystrength = (int((strength/5)+1))
        display.show(str(displaystrength))
        sleep(20)
# creates a color spectrum from red to blue
        #full red
        if displaystrength == 10:
            set_rgb(1023, 0, 1023)
            sleep(20)
        if displaystrength == 9:
            set_rgb(1023, 100, 900)
            sleep(20)
        if displaystrength == 8:
            set_rgb(1023, 200, 700)
            sleep(20)
        if displaystrength == 7:
            set_rgb(1023, 400, 500)
            sleep(20)
        if displaystrength == 6:
            set_rgb(1023, 600, 300)
            sleep(20)
        if displaystrength == 5:
            set_rgb(1023, 800, 100)
            sleep(20)
        if displaystrength == 4:
            set_rgb(900, 900, 100)
            sleep(20)
        if displaystrength == 3:
            set_rgb(800, 1023, 100)
            sleep(20)
        if displaystrength == 2:
            set_rgb(600, 1023, 300)
            sleep(20)
        if displaystrength == 1:
            set_rgb(400, 1023, 500)
            sleep(20)
# if pulse sensor is pressed on beacon, the led will blink 3 times
    if incoming == '2':
        set_rgb(1023, 0, 1023)
        sleep(100)
        set_rgb(1023, 1023, 1023)
        sleep(500)
        set_rgb(1023, 0, 1023)
        sleep(100)
        set_rgb(1023, 1023, 1023)
        sleep(500)
        set_rgb(1023, 0, 1023)
        sleep(100)
        set_rgb(1023, 1023, 1023)
        sleep(500)