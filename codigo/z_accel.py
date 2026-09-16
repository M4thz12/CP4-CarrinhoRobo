from picar import back_wheels
import time

bw = back_wheels.Back_Wheels(debug=True)

print("PWM A:", bw.PWM_A)
print("PWM B:", bw.PWM_B)

bw.speed = 30
bw.backward()

time.sleep(1)
bw.speed = 50
time.sleep(1)
bw.speed = 100

time.sleep(2)
bw.stop()

time.sleep(2)
bw.forward()



bw.stop()
