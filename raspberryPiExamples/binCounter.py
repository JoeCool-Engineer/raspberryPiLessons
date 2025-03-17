import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
pins = [29, 31, 33, 35, 37]
gpio.setup(pins, gpio.OUT)

ledOn = True
ledOff = False

gpio.output(pins, ledOff)
for i in range(0, 32, 1):
	time.sleep(1)
	if i>=16:
		gpio.output(37, ledOn)
		i = i%16
	if i>=8:
		gpio.output(35, ledOn)
		i = i%8
	if i>=4:
		gpio.output(33, ledOn)
		i = i%4
	if i>=2:
		gpio.output(31, ledOn)
		i = i%2
	if i>=1:
		gpio.output(29, ledOn)
	if i==0:
		gpio.output(29, ledOff)
	time.sleep(1)
	gpio.output(pins, ledOff)

gpio.cleanup()


