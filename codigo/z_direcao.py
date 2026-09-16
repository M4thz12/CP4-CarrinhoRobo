from picar import front_wheels
import time

fw = front_wheels.Front_Wheels(debug=True)

print("Canal:", fw.channel)

fw.turn_straight()
time.sleep(1)
fw.turn_right()
time.sleep(1)
fw.turn_straight()
time.sleep(1)
fw.turn_left()
time.sleep(1)
fw.turn_straight()
