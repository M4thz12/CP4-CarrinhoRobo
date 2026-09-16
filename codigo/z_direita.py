from picar import front_wheels
import time

fw = front_wheels.Front_Wheels(debug=True)

print("Canal:", fw.channel)

fw.turn_right()
time.sleep(1)
