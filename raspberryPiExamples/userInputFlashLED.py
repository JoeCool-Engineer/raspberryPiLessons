import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

ledOn = True
ledOff = False

userInput = 'Y'
while userInput == 'Y':
	ledFlash = int(input("How many times would you like to flash the led: "))
	for i in range(0,ledFlash,1):
		GPIO.output(37, ledOn)
		time.sleep(.1)
		GPIO.output(37, ledOff)
		time.sleep(.1)
		GPIO.output(36, ledOn)
		time.sleep(.1)
		GPIO.output(36, ledOff)
		time.sleep(.1)
	userInput = input("Would you like to continue (Y for Yes): ")
 
GPIO.cleanup()
