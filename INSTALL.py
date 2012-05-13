#!/usr/bin/python

import os;

os.system('sudo mkdir /opt/HomeAutomation');
os.system('sudo mkdir /opt/HomeAutomation/Config');
os.system('sudo mkdir /opt/HomeAutomation/Scripts');
os.system('sudo mkdir /opt/HomeAutomation/Schedule');
os.system('sudo mkdir /opt/HomeAutomation/Sensors');

os.system('sudo chown pi /opt/HomeAutomation');
os.system('sudo chown pi /opt/HomeAutomation/Config');
os.system('sudo chown pi /opt/HomeAutomation/Scripts');
os.system('sudo chown pi /opt/HomeAutomation/Schedule');
os.system('sudo chown pi /opt/HomeAutomation/Sensors');

os.system('sudo cp -r $PWD/* /opt/HomeAutomation');

print "Installation complete!";
print;
print "App has been installed to: /opt/HomeAutomation/";
