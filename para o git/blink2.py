from gpiozero import LED
from time import sleep

#PINs dos LEDs
pin = LED(18)
pin2 = LED(15)

while 1:
	pin.on() 	#Led 1 on
	sleep(1) 	#Delay
	pin.off()	#LED 1 off
	pin2.on()	#Led 2 on
	sleep(0.5)	#Delay
	pin2.off()	#Led 2 off

