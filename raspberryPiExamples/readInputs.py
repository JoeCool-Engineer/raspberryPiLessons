import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD) #Reading the physical pins
inPin = 40
gpio.setup(inPin, gpio.IN)

try:
	while True:
		readVal = gpio.input(inPin)
		print(readVal)
		sleep(1)

except KeyboardInterrupt:
	gpio.cleanup()

