# Servo Control

import time

class Servo():
    def set(self, property, value):
        try:
            # PWM is GPIO PIN 18 (board PIN 12)
            f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
            f.write(value)
            f.close()   
        except:
            print("Error writing to: " + property + " value: " + value)

    def setServo(self, angle):
        self.set("servo", str(angle))
    
    def run(self):
        self.set("delayed", "0")
        self.set("mode", "servo")
        self.set("servo_max", "180")
        self.set("active", "1")

        delay_period = 0.008

        for angle in range(0, 180):
            self.setServo(angle)
            time.sleep(delay_period)

        self.setServo(90)

if __name__ == '__main__':
    servo = Servo()
    servo.run()
