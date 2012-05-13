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
		# Pause
		x = raw_input("Press Enter to Return to Menu");   
         
def ScheduleEdit():
    # Edit the master schedule with nano
	os.system('nano /home/pi/.homeautomation/Schedule/schedule');
	# Recreate the days schedule
    Scheduleimport();
    
def SensorCheck(Currenttime,Temprate):
    try:
		# Open the first sensors data file
		sensorfile = open('/home/pi/.homeautomation/Sensors/1', 'r');
		sensordata = sensorfile.read();
		# Create a list from the csv data
		split = shlex.shlex(sensordata);
		split.whitespace += ',';
		split.whitespace_split = True;
		sensorstats = list(split);
		# Populate the Sensor variables from the list
		Sensortype = sensorstats[0];
		Sensortemp = sensorstats[1];
    except:
		print "Error: Could not get sensor stats.";
	# Kick-off the next function
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

	# Check the sensor type and correct accordingly
    if Sensortype == "v":
        Sensortype = "Virtual Sensor";
    elif Sensortype == "p":
        Sensortype = "Physical Sensor";
	
	# Kick-off the next function
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

	# Kick-off the next function
    Display(strCurrenttime,strSchedtemp,strSensortemp,Sensortemp,Sensortype,strTempdiff,Tempdiff,strTemptimereq);
 
def Display(strCurrenttime,strSchedtemp,strSensortemp,Sensortemp,Sensortype,strTempdiff,Tempdiff,strTemptimereq):
    # Print system status
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
    # Check whether heater or fan is applicable
	if Tempdiff > 0:
        print "The heater will be activated for", strTemptimereq;
    else:
        print "The fan will be activated for", strTemptimereq[1:]
    print;
	# Pause
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
	# Input prompt
    return input ("Option: ");

# Start app
loop = 1
choice = 0
# Start main menu and wait for option
while loop == 1:
    choice = Menu();
    if choice == 1:
		# Clear screen
        os.system('clear');
		# Start monitor cycle
        SensorCheck(Currenttime,Temprate);
    elif choice == 2:
		# Clear screen
        os.system('clear');
		# Recreate todays schedule
        Scheduleimport();
    elif choice == 3:
		# Clear screen
        os.system('clear');
		# Edit the master schedule
        ScheduleEdit();
    elif choice == 4:
		# Clear screen
        os.system('clear');
		# Break from loop (exit)
        break;