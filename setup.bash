#!/bin/bash

echo "sudo apt-get update"
sudo apt-get update
echo "sudo apt-get upgrade"
sudo apt-get upgrade
echo "sudo apt-get clean"
sudo apt-get clean
echo "sudo apt-get install python-dev"
sudo apt-get install python-dev
echo "sudo apt-get install python-pip"
sudo apt-get install python-pip
echo "sudo apt-get install python-mysqldb"
sudo apt-get install python-mysqldb
echo "sudo apt-get install git"
sudo apt-get install git
echo "sudo apt-get install node"
sudo apt-get install node
echo "sudo apt-get install npm"
sudo apt-get install npm
echo "sudo apt-get install mysql-server"
sudo apt-get install mysql-server
echo "git clone https://github.com/adafruit/Adafruit_Python_DHT.git"
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
echo "cd Adafruit_Python_DHT"
cd Adafruit_Python_DHT
echo "sudo python setup.py install"
sudo python setup.py install
echo "cd .."
cd ..
echo "sudo rm -r Adafruit_Python_DHT"
sudo rm -r Adafruit_Python_DHT


