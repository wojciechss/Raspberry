#!/usr/bin/python3

import cv2


class BallDetector:

    def __init__(self):
        self.greenLower = (29, 86, 6)
        self.greenUpper = (64, 255, 255)

    def detect(self, img):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.greenLower, self.greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            m = cv2.moments(c)
            return [[int(m["m10"] / m["m00"]), int(m["m01"] / m["m00"]), radius]]
        return []
