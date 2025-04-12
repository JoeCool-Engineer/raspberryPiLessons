import RPi.GPIO as gpio
from time import sleep

delay = .1
inPin = 40
outPin = 38

gpio.setmode(gpio.BOARD)
gpio.setup(outPin, gpio.OUT)
gpio.setup(inPin, gpio.IN, pull_up_down=gpio.PUD_UP)

ledState = 0
buttonState = 1
buttonStateOld = 1

try:
	while True:
		buttonState = gpio.input(inPin)
		if buttonState == 1 and buttonStateOld == 0:
			if ledState == 1:
				ledState = 0
				gpio.output(outPin, ledState)
				print("Led Off")
			else:
				ledState = 1
				gpio.output(outPin, ledState)
				print("Led On")
				
		buttonStateOld = buttonState
		sleep(delay)

except KeyboardInterrupt:
	gpio.cleanup()
	print("GPIO Pin Ready to Go")