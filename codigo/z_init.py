from picar.SunFounder_PCA9685 import PCA9685

pwm = PCA9685.PWM(bus_number=1, address=0x40)
pwm.setup()

print("PCA9685 OK")
