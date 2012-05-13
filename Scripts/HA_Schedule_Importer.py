#!/usr/bin/python

# System imports
import sys;
from time import localtime;

schedule = []

# Read master schedule from file 'schedule'
def ReadMaster(schedule):
    try:
        schedule = [line.strip() for line in open('/home/pi/.homeautomation/Schedule/schedule')];
        WriteToday(schedule);
    except:
        print "Error: Unable to open master schedule.";

# Write todays schedule to file 'schedule_today'
def WriteToday(schedule):
    try:
        schedfile = open('/home/pi/.homeautomation/Schedule/schedule_today', 'w');
        schedtoday = str(schedule[localtime()[6]]);
        schedfile.write(schedtoday);
        print "Todays schedule has been created!";
    except:
        print "Error: Unable to write todays schedule.";

ReadMaster(schedule);