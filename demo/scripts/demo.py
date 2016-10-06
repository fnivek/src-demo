#!/usr/bin/env python
"""This is a demo."""

import rospy
import cv2


def main():
    """Main function."""
    rospy.init_node('demo')

    cv2.namedWindow('demo', cv2.WINDOW_AUTOSIZE)

    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    while not rospy.is_shutdown():
        _, frame = cap.read()
        cv2.imshow('demo', frame)

        key = 0xFF & cv2.waitKey(10)
        if key == 0x1B:
            break

if __name__ == '__main__':
    main()
