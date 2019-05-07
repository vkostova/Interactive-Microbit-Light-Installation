from microbit import *
import neopixel
import random
import radio
id = "1"

# low power so the other receiver has to get close
radio.config(power=1)
radio.on()

# Setup the Neopixel strip on pin0 with a length of 24 LEDs
num_pixels = 24
np = neopixel.NeoPixel(pin0, num_pixels)


# Color Palettes 
cool = [
    (0, 255, 0),        # green
    (0, 255, 40),       # jade 
    (173, 255, 47),     # green yellow 
    (240, 255, 255),    # azure 
    (50, 255, 255),     # aqua 
    (0, 255, 120),      # teal 
    (0, 255, 255),      # cyan 
    (0, 0, 255),        # blue 
    (180, 0, 255),      # purple
    (255, 0, 20),       # magenta 
]

warm = [
    (255, 0, 0),        # red 
    (242, 90, 255),     # pink 
    (255, 20, 147),     # deep pink 
    (250, 128, 114),    # salmon 
    (255, 100, 0),      # amber 
    (255, 40, 0),       # orange
]


all_colors = [
    (255, 0, 0),        # red 
    (242, 90, 255),     # pink 
    (255, 20, 147),     # deep pink 
    (250, 128, 114),    # salmon 
    (255, 150, 0),      # yellow 
    (255, 100, 0),      # amber 
    (255, 40, 0),       # orange
    (0, 255, 0),        # green
    (0, 255, 40),       # jade 
    (173, 255, 47),     # green yellow
    (240, 255, 255),    # azure 
    (50, 255, 255),     # aqua
    (0, 255, 120),      # teal 
    (0, 255, 255),      # cyan 
    (0, 0, 255),        # blue
    (180, 0, 255),      # purple
    (255, 0, 20),       # magenta 
]


palette2 = [
    (255, 255, 255),    # white 
    (0, 0, 255),        # blue 
    (0, 255, 120),      # teal 
    (0, 255, 255),      # cyan 
]

black = (0, 0, 0)           # clear
white = (255, 255, 255)     # rest

# heart pulse
milliseconds_per_second = 1000  # Timing settings
sampling_rate = 15  # (Hz) typically 25-100 samples per second
sampling_interval = int(milliseconds_per_second / sampling_rate)
samples_between_beats = 0  # count how many samples occur between beats.

display.off() 

while True:
    radio.send(id)
    # read signal from input in pin 3
    # print pulse and sample count from 1
    # display in plotter and REPL 
    # set LED to a random number from 0 - 24, in increments of 5
    # if pulse is less than #, display colors
    
    sleep(0.01) 
    pulse = pin2.read_analog()   
    print("({}, {})".format((pulse), samples_between_beats))
    samples_between_beats += 1

    for i in range(0, 24, 1):
        
        if pulse < 100:
            np[i] = (random.choice(warm))   # set assigned LEDS to warm colors
            np.show()                       # display the lights on the neopixel
            radio.send('2')
        else:
            np[i] = (random.choice(cool))     # set neopixel to cool colors
            np.show()                         # display the colors on the np
        sleep(sampling_interval)
