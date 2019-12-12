#!/usr/bin/env python
import rospy
#import RPi.GPIO as GPIO
import pandas as pd
import std_msgs.msg
from std_msgs.msg import Float32MultiArray

# Instancia DataFrame 
df = pd.DataFrame(columns=['TimeStamp', 'Value'])

# Lê valores do tópico e adiciona no DataFrame
def leitura(pot):
    timestamp = pd.datetime.now().time()
    for i in range(6):
        new_row = {'TimeStamp':timestamp, 'Value':pot[i]}
        df = df.append(new_row, ignore_index=True)

def callback(msg):
    leitura(msg.data)


if __name__ == '__main__':

	rospy.init_node('topic_read_subscriber')
	sub = rospy.Subscriber('Potenciometro', Float32MultiArray, callback)
	#while not rospy.is_shutdown():
	#	rospy.spin()

#Exporta DataFrame
df.to_csv("/home/ubuntu/exp_plot.csv", encoding='utf-8', index=False)
