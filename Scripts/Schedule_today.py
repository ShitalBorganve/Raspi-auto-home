#!/usr/bin/python

# System imports
import sys;
from time import localtime;

# Variables
schedule = [];

# Read master schedule from file 'schedule'
def ReadMaster(schedule):
    try:
        # Read in master schedule line per list entry
        schedule = [line.strip() for line in open('/opt/HomeAutomation/Schedule/schedule')];
        # Kick-off next function passing schedule list
        WriteToday(schedule);
    except:
        print "Error: Unable to open master schedule.";

# Write todays schedule to file 'schedule_today'
def WriteToday(schedule):
    try:
        # Open todays schedule file
        schedfile = open('/opt/HomeAutomation/Schedule/schedule_today', 'w');
        # Search schedule list for today
        schedtoday = str(schedule[localtime()[6]]);
        # Write todays schedule to file
        schedfile.write(schedtoday);
        print "Todays schedule has been created!";
    except:
        print "Error: Unable to write todays schedule.";

# Start App
ReadMaster(schedule);