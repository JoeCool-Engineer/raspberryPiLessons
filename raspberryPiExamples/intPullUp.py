from time import sleep
import RPi.GPIO as gpio

delay = .1
inPin = 40
outPin = 38
gpio.setmode(gpio.BOARD)
gpio.setup(outPin, gpio.OUT)
gpio.setup(inPin, gpio.IN, pull_up_down=gpio.PUD_UP)

try:
	while True:
		readVal = gpio.input(inPin)
		print(readVal)
		if readVal == 1:
			gpio.output(outPin, 1)
		if readVal == 0:
			gpio.output(outPin, 0)
		sleep(delay)

except KeyboardInterrupt:
	gpio.cleanup()
	print("GPIO Ready to Go")
