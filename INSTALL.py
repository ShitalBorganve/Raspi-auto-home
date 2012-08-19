#!/usr/bin/python

import os;

os.system('sudo mkdir ~/Raspi-auto-home');
os.system('sudo mkdir ~/Raspi-auto-home/Config');
os.system('sudo mkdir ~/Raspi-auto-home/Scripts');
os.system('sudo mkdir ~/Raspi-auto-home/Schedule');
os.system('sudo mkdir ~/Raspi-auto-home/Sensors');

os.system('sudo chown $LOGNAME ~/Raspi-auto-home/');
os.system('sudo chown $LOGNAME ~/Raspi-auto-home/Config');
os.system('sudo chown $LOGNAME ~/Raspi-auto-home/Scripts');
os.system('sudo chown $LOGNAME ~/Raspi-auto-home/Schedule');
os.system('sudo chown $LOGNAME ~/Raspi-auto-home/Sensors');

os.system('sudo cp -r $PWD/* ~/Raspi-auto-home/');

print "Installation complete!";
