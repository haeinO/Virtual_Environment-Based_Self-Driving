#!/usr/bin/env python
  
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, CompressedImage


class IMGParser:
    def __init__(self):
        global img_bgr
        rospy.init_node('camera', anonymous=True)
    
        self.image_sub = rospy.Subscriber("/image_jpeg/compressed", CompressedImage, self.callback)
        self.img_bgr = 0
        self.gray = 0
        #rospy.spin()

    def callback(self, data):
        
        np_arr = np.fromstring(data.data, np.uint8)
        self.img_bgr = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        self.gray = cv2.cvtColor(self.img_bgr, cv2.COLOR_BGR2GRAY)
        print(self.img_bgr)
        cv2.imshow("Image window", self.gray)
        cv2.waitKey(1)

        #cv2.imshow("Image window2", self.img_bgr)
        #cv2.waitKey(1)
        
    #def draw(self):
    #    rsquare = cv2.rectangle(self.img_bgr, (100, 300), (450, 340), (0, 255, 0), 3)
                                    
    #    print(self.img_bgr)

    #    print("123123")
                                    
if __name__ == '__main__':
    #try:
    while not rospy.is_shutdown():
        image_parser = IMGParser() 
        image_parser.draw()
        rospy.spin()
    #except rospy.ROSInterruptException:
        #pass