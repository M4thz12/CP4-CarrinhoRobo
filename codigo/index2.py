import time
import RPi.GPIO as GPIO

class Ultrasonic:
    def __init__(self):
        self.trigger_pin = 20
        self.echo_pin = 21
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def get_distance(self):
        """Retorna a distância medida em centímetros (cm)"""
        # Envia pulso de 10us no Trigger
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, GPIO.LOW)

        # Aguarda a resposta no pino Echo
        while GPIO.input(self.echo_pin) == 0:
            pass
        pulse_start = time.time()

        while GPIO.input(self.echo_pin) == 1:
            pass
        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        # Velocidade do som (~34300 cm/s) dividida por 2
        distance = round(pulse_duration * 17150, 2)
        return distance

if __name__ == '__main__':
    sensor = Ultrasonic()
    try:
        while True:
            dist = sensor.get_distance()
            print(f"Distância do obstáculo: {dist} cm")
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()