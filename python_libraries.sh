#!/bin/bash
#Author:  William Miller
#Date:    3-7-18
#Purpose: Download commonly used Python libraries and other software
#Notes:   To run--> go to directory of this file and type ./python_libraries.sh in command line"

echo "==============================================="
echo "adding repository for unetbootin:"
sudo add-apt-repository ppa:gezakovacs/ppa
sudo apt-get update
echo "==============================================="

echo "==============================================="
echo "Downloading Unetbootin..."
sudo apt-get install unetbootin
echo "==============================================="

echo "==============================================="
echo "Downloading Arduino IDE:"
sudo sudo apt-get update && sudo apt-get install arduino arduino-core
echo "==============================================="

echo "==============================================="
echo "Downloading Python Libraries...."
echo "==============================================="

echo "==============================================="
echo "numpy:"
sudo apt-get install python3-numpy
echo "==============================================="

echo "==============================================="
echo "scipy:"
sudo apt-get install python3-scipy
echo "==============================================="

echo "==============================================="
echo "beautifulsoup4:"
sudo apt-get install python3-bs4
echo "==============================================="

echo "==============================================="
echo "pandas:"
sudo apt-get install python3-pandas
echo "==============================================="

echo "==============================================="
echo "tkinter:"
sudo apt-get install python3-tk
echo "==============================================="

echo "==============================================="
echo "pandas-datareader:"
sudo -H pip3 install pandas-datareader
echo "==============================================="

echo "==============================================="
echo "scikit-learn:"
sudo -H pip3 install scikit-learn
echo "==============================================="

echo "==============================================="
echo "matplotlib:"
sudo -H pip3 install matplotlib
echo "==============================================="

echo "==============================================="
echo "pyserial (for communication between Arduino and python):"
sudo -H pip3 install pyserial
echo "==============================================="


#END
