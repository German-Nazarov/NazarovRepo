import RPi.GPIO as GPIO
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
led = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(led, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
#[GPIO.setup(i, GPIO.OUT, initial=GPIO.LOW) for i in dac] 
#value = 0

def binary(n):
    ans = [int(x) for x in bin(n)[2::].zfill(8)]
    return ans



def adc_f():
    sum = 0
    for i in range(1, 9):
        array = binary(int(256 / 2**i + sum))
        GPIO.output(dac, array)
        time.sleep(0.01)
        compvlt = GPIO.input(comp)
        if (compvlt) == 1:
            sum += int(256/2**i)
    return sum

try:
    while True:
        for i in range(255):
            
            num = adc_f()
            real_volts = int(3.3 * num/256*100)/100
            percent = (real_volts/3.3)*100
            led_percent = int((percent/100) * 8)
            for j in range(7, 0, -1):
                if (j < led_percent):
                    GPIO.output(led[j], 0)
                else:
                    GPIO.output(led[j], 1)
            if num>0:
                print(num, real_volts, percent)
                

finally:
    [GPIO.output(i, 0) for i in dac]
    GPIO.cleanup()