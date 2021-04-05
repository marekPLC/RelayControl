import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relayNum = [17, 18]
timeDelay = int(10)

def relay(x, y):
        t0 = time.time()
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, GPIO.HIGH)
        print("Relay" + str(x) +" = TRUE")
        time.sleep(y)
        GPIO.output(x, GPIO.LOW)
        print("Relay" + str(x) + " = FALSE")
        t1 = time.time()
        total = t1-t0
        return round(total, 1)

print("Proces trval "  + str(relay(relayNum[0], timeDelay))+ "s.\n" + "Kontakt c. " + str(relayNum[0]) + " a delayem" + " " + str(timeDelay))
print("Proces trval " + str(relay(relayNum[1], timeDelay))+ "s.\n" + "Kontakt c. " + str(relayNum[1]) + " a delayem" + " " + str(timeDelay))
