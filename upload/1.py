from Motor import *
#This is just a template for you the setMotorModel function lets the user set the speed for each motor.
#Using the sleep function it will let the motor run for that amount of seconds then switch to its next command eventually ending with another sleep
PWM=Motor()


#PWM.setMotorModel(speed,speed,speed,speed) heres a model for reference. The speed can go from -2000 to 2000

PWM.setMotorModel(1000,1000,1000,1000)       #Forward
time.sleep(1)
PWM.setMotorModel(-1000,-1000,-1000,-1000)   #Back
time.sleep(1)
PWM.setMotorModel(-150,-150,200,200)       #Left
time.sleep(1)
PWM.setMotorModel(200,200,-100,-100)       #Right
time.sleep(1)













#Do not remove this sleep
PWM.setMotorModel(0,0,0,0)                   #Stop



