import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD) #Reading the physical pins
inPin = 40
outPin = 38
gpio.setup(inPin, gpio.IN)
gpio.setup(outPin, gpio.OUT)

try:
	while True:
		readVal = gpio.input(inPin)
		ledOn = True
		ledOff = False
		if readVal == 1:
			gpio.output(outPin, ledOn)
			print("Led On")
		if readVal == 0:
			gpio.output(outPin, ledOff)
			print("Led Off")
		sleep(1)

except KeyboardInterrupt:
	gpio.cleanup()

