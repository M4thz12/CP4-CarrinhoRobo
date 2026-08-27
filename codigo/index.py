import time
import RPi.GPIO as GPIO

class Motor:
    def __init__(self):
        # Mapeamento dos pinos GPIO (padrão BCM)
        self.PWMA = 18  # Velocidade Motor A
        self.AIN1 = 22  # Direção Motor A (Pino 1)
        self.AIN2 = 27  # Direção Motor A (Pino 2)
        
        self.PWMB = 23  # Velocidade Motor B
        self.BIN1 = 25  # Direção Motor B (Pino 1)
        self.BIN2 = 24  # Direção Motor B (Pino 2)
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        # Configura todos os pinos como saída
        for pin in (self.PWMA, self.AIN1, self.AIN2, self.PWMB, self.BIN1, self.BIN2):
            GPIO.setup(pin, GPIO.OUT)
            
        # Inicializa o controle PWM (frequência 1000Hz)
        self.pwm_a = GPIO.PWM(self.PWMA, 1000)
        self.pwm_b = GPIO.PWM(self.PWMB, 1000)
        self.pwm_a.start(0)
        self.pwm_b.start(0)

    def move_forward(self, speed=50):
        """Move o carrinho para frente"""
        GPIO.output(self.AIN1, GPIO.HIGH)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.HIGH)
        GPIO.output(self.BIN2, GPIO.LOW)
        self.pwm_a.ChangeDutyCycle(speed)
        self.pwm_b.ChangeDutyCycle(speed)

    def move_backward(self, speed=50):
        """Move o carrinho para trás"""
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.HIGH)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.HIGH)
        self.pwm_a.ChangeDutyCycle(speed)
        self.pwm_b.ChangeDutyCycle(speed)

    def stop(self):
        """Para totalmente os motores"""
        self.pwm_a.ChangeDutyCycle(0)
        self.pwm_b.ChangeDutyCycle(0)
        GPIO.output(self.AIN1, GPIO.LOW)
        GPIO.output(self.AIN2, GPIO.LOW)
        GPIO.output(self.BIN1, GPIO.LOW)
        GPIO.output(self.BIN2, GPIO.LOW)

if __name__ == '__main__':
    car_motor = Motor()
    try:
        print("Movendo para frente...")
        car_motor.move_forward(60)
        time.sleep(2)
        
        print("Parando...")
        car_motor.stop()
        time.sleep(1)
        
        print("Movendo para trás...")
        car_motor.move_backward(60)
        time.sleep(2)
        
        car_motor.stop()
        print("Teste concluído!")
    except KeyboardInterrupt:
        car_motor.stop()
        GPIO.cleanup()