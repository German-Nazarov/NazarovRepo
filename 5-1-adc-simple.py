import RPi.GPIO as GPIO
import sys
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.output(troyka, 1)
#value = 0

def binary(n):
    ans = [int(x) for x in bin(n)[2::].zfill(8)]
    return ans

def adc():
    for i in range(256):
        dac_v = binary(i)
        GPIO.output(dac,dac_v)
        comp_value = GPIO.input(comp)
        time.sleep(0.005)
        if(comp_value == 0):
            return i

try:
    while True:
        k = adc()
        if k!=0:
            print(k, '{:.2f}v'.format(3.3*k/256))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

