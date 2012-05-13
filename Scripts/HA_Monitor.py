#!/usr/bin/python

# Imports
import sys, os, shlex;
from time import localtime;

# Variables
Currenttime = localtime()[3];
Temprate = 1;

# Define Functions
def Scheduleimport():
        print "                     Schedule Import";
        print;
        print "Starting Import...";
        try:
            #Run Schedule Importer script to create schedule_today file
            os.system('./home/pi/HA_Schedule_Importer.py');
        except:
                print "Error: Could not run Schedule Importer script.";
        print;
        x = raw_input("Press Enter to Return to Menu");   
         
def ScheduleEdit():
    os.system('nano /home/pi/.homeautomation/Schedule/schedule');
    Scheduleimport();
    
def SensorCheck(Currenttime,Temprate):
    sensorfile = open('/home/pi/.homeautomation/Sensors/1', 'r');
    sensordata = sensorfile.read();
    split = shlex.shlex(sensordata);
    split.whitespace += ',';
    split.whitespace_split = True;
    sensorstats = list(split);
    Sensortype = sensorstats[0];
    Sensortemp = sensorstats[1];
    
    Processing(Currenttime,Sensortemp,Sensortype,Temprate);

def Processing(Currenttime,Sensortemp,Sensortype,Temprate):
    # Read todays schedule file
    schedfile = open('/home/pi/.homeautomation/Schedule/schedule_today', 'r');
    Schedule = schedfile.read();

    # Split 'Schedule' into comma separated list
    split = shlex.shlex(Schedule);
    split.whitespace += ',';
    split.whitespace_split = True;
    Schedule = list(split);

    # Set Schedtemp as this hours value in the list
    Schedtemp = Schedule[Currenttime + 1];

    # Calculate temperature difference
    Tempdiff = int(Schedtemp) - int(Sensortemp);

    # Calculate heating time req
    Temptimereq = Tempdiff / Temprate;

    if Sensortype == "v":
        Sensortype = "Virtual Sensor";
    elif Sensortype == "p":
        Sensortype = "Physical Sensor";

    Formatting(Currenttime,Schedtemp,Sensortemp,Sensortype,Tempdiff,Temptimereq);

    

def Formatting(Currenttime,Schedtemp,Sensortemp,Sensortype,Tempdiff,Temptimereq):
    # Format time string
    strCurrenttime = str(Currenttime);
    strCurrenttime += ":00";

    # Format schedule temperature string
    strSchedtemp = str(Schedtemp);
    strSchedtemp += "*C";

    # Format sensor temperature string
    strSensortemp = str(Sensortemp);
    strSensortemp += "*C";

    # Format temperature difference string
    strTempdiff = str(Tempdiff);
    strTempdiff += "*C";

    # Format heating time string
    strTemptimereq = str(Temptimereq);
    strTemptimereq += " mins";

    Display(strCurrenttime,strSchedtemp,strSensortemp,Sensortemp,Sensortype,strTempdiff,Tempdiff,strTemptimereq);
 

def Display(strCurrenttime,strSchedtemp,strSensortemp,Sensortemp,Sensortype,strTempdiff,Tempdiff,strTemptimereq):
    print "                     System Monitor";
    print;
    print "##############";
    print "#  Overview  #";
    print "##############";
    print;
    print "No. of sensors reporting: ", "1", Sensortype;
    print;
    print;
    print "###############";
    print "# Temperature #";
    print "###############";
    print;
    print "The temperature at", strCurrenttime, "should be", strSchedtemp;
    print "The temperature is currently:", strSensortemp;
    print "This is a difference of:", strTempdiff;
    if Tempdiff > 0:
        print "The heater will be activated for", strTemptimereq;
    else:
        print "The fan will be activated for", strTemptimereq[1:]
    print;
    x = raw_input("Press Enter to Return to Menu");

def Menu():
    # Clear screen
    os.system('clear');
    # Main menu
    print "                     Home Automation System";
    print "Main Menu:";
    print;
    print "1) System Monitor";
    print "2) Import Schedule";
    print "3) Edit Schedule";
    print "4) Exit";
    print;
    return input ("Option: ");

# Start
loop = 1
choice = 0
while loop == 1:
    choice = Menu();
    if choice == 1:
        os.system('clear');
        SensorCheck(Currenttime,Temprate);
    elif choice == 2:
        os.system('clear');
        Scheduleimport();
    elif choice == 3:
        os.system('clear');
        ScheduleEdit();
    elif choice == 4:
        os.system('clear');
        break;