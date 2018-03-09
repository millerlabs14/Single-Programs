#!/bin/bash
#Author:  William Miller
#Date:    3-7-18
#Purpose: Download commonly used Python libraries
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

#END
