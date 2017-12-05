#!/usr/bin/env python
import sys
import numpy as np
import rospy
from std_msgs.msg import Float32

def sinusPub(f=0.5, f_s = 100, volume = 1.0):
    pub = rospy.Publisher('sinus', Float32, queue_size=10)
    rospy.init_node('sinus', anonymous=True)
    rate = rospy.Rate(f_s)
    
    signal = volume * np.sin(np.linspace(0, 2*np.pi, f_s/f))

    while not rospy.is_shutdown():
        for sinVal in signal:
          pub.publish(sinVal)
          rate.sleep()

if __name__ == '__main__':
  if len(sys.argv) > 4:
    print "Usage: " + sys.argv[0] + " [frequency] [sample frequency] [amplitude]"
  elif len(sys.argv) > 3:
    try:
      sinusPub(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    except rospy.ROSInterruptException:
      pass
  elif len(sys.argv) > 2:
    try:
      sinusPub(float(sys.argv[1]), float(sys.argv[2]))
    except rospy.ROSInterruptException:
      pass
  elif len(sys.argv) > 1:
    try:
      sinusPub(float(sys.argv[1]))
    except rospy.ROSInterruptException:
      pass
  else:
    try:
      sinusPub()
    except rospy.ROSInterruptException:
      pass