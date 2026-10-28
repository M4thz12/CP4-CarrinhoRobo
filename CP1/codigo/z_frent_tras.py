from picar import back_wheels
import time



bw = back_wheels.Back_Wheels(debug=True)


print("PWM A:", bw.PWM_A)
print("PWM B:", bw.PWM_B)


bw.speed = 30
bw.forward()
time.sleep(5)

bw.stop()
time.sleep(1)


bw.backward()
time.sleep(5)

bw.stop()
time.sleep(1)
