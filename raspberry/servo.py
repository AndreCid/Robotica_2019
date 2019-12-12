import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

servo_1_Pin = 40
servo_2_Pin = 37
servo_3_Pin = 38
servo_4_Pin = 36
servo_5_Pin = 35
servo_6_Pin = 33

GPIO.setup(servo_1_Pin,GPIO.OUT)
GPIO.setup(servo_2_Pin,GPIO.OUT)
GPIO.setup(servo_3_Pin,GPIO.OUT)
GPIO.setup(servo_4_Pin,GPIO.OUT)
GPIO.setup(servo_5_Pin,GPIO.OUT)
GPIO.setup(servo_6_Pin,GPIO.OUT)

pwm_1=GPIO.PWM(servo_1_Pin,50)
pwm_2=GPIO.PWM(servo_2_Pin,50)
pwm_3=GPIO.PWM(servo_3_Pin,50)
pwm_4=GPIO.PWM(servo_4_Pin,50)
pwm_5=GPIO.PWM(servo_5_Pin,50)
pwm_6=GPIO.PWM(servo_6_Pin,50)

pwm_1.start(0)
pwm_2.start(0)
pwm_3.start(0)
pwm_4.start(0)
pwm_5.start(0)
pwm_6.start(0)

flag = 1
while flag == 1:
	desiredAngle_1 = input('Angulo_1 desejado:')
	desiredAngle_2 = input('Angulo_2 desejado:')
	desiredAngle_3 = input('Angulo_3 desejado:')
	desiredAngle_4 = input('Angulo_4 desejado:')
	desiredAngle_5 = input('Angulo_5 desejado:')
	desiredAngle_6 = input('Angulo_6 desejado:')
	
	if desiredAngle_3 < 15:
		desiredAngle_3 = 15
	if desiredAngle_4 < 10:
		desiredAngle_4 = 10
	if desiredAngle_5 > 170:
		desiredAngle_5 = 170

	DC_1 = 1./18.*(desiredAngle_1)+2
	pwm_1.ChangeDutyCycle(DC_1)
	time.sleep(1)

	DC_2 = 1./18.*(desiredAngle_2)+2
	pwm_2.ChangeDutyCycle(DC_2)
	time.sleep(1)

	DC_3 = 1./18.*(desiredAngle_3)+2
	pwm_3.ChangeDutyCycle(DC_3)
	time.sleep(1)

	DC_4 = 1./18.*(desiredAngle_4)+2
	pwm_4.ChangeDutyCycle(DC_4)
	time.sleep(1)

	DC_5 = 1./18.*(desiredAngle_5)+2
	pwm_5.ChangeDutyCycle(DC_5)
	time.sleep(1)

	DC_6 = 1./18.*(desiredAngle_6)+2
	pwm_6.ChangeDutyCycle(DC_6)
	time.sleep(1)

	flag = input('Deseja continuar? 1/0')

pwm_1.stop()
pwm_2.stop()
pwm_3.stop()
pwm_4.stop()
pwm_5.stop()
pwm_6.stop()

GPIO.cleanup()
