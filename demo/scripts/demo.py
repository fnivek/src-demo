#!/usr/bin/env python
"""This is a demo."""

import rospy


def main():
    """Main function."""
    rospy.init_node('demo')

    while not rospy.is_shutdown():
        rospy.loginfo('Running!')

if __name__ == '__main__':
    main()
