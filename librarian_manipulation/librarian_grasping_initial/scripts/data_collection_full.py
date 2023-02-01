#!/usr/bin/env python3

import random
import rospy
from std_msgs.msg import String
import os

rospy.init_node('full_data_collector')
books = ['w','r','y']
f = open('full_data.txt', 'a+')
if os.stat('full_data.txt').st_size == 0:
    f.write('Data for the experiment of executing the full pick and place pipeline. In the following, w will stand for the white book, r for the red book and y for the yellow book. Further, s will stand for an successful attempt and f for a failure. \n')
    f.write('attempt | book_order | outcome \n')
    attempt = 0
else:
    f2 = open('attempts.txt', 'r')
    attempt = int(f2.readline())
    f2.close()
pub = rospy.Publisher('chatter', String, queue_size = 10)

while True:
    attempt += 1
    sequence = random.sample(books, len(books))
    print("Attempt nr. {} has the book sequence {}. Please place the books in the correct positions, and prepare the robot for the next run.".format(attempt, sequence))
    input("Please press Enter when ready for the next run.")
    pub.publish('sort')
    outcome = input("Please enter a series of 3 letters, s for success or f for failure, for each of the books of the last run.")
    f.write("{} | {} | {} \n".format(attempt, sequence, outcome))
    print("Experiment finished and written to the output file.")
    print("Robot will now reset its arms, please prepare to catch the book.")
    os.system("rosrun librarian_grasping_initial reset_arms.py default")
    cont = input("Please press c if another experiment shall be run.")
    if cont != 'c':
        f2 = open('attempts.txt', 'w')
        f2.write(str(attempt))
        f2.close()
        break

f.close()
