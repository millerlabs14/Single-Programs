#!/bin/bash
#Author:  William Miller
#Date:    3-7-18
#Purpose: Download commonly used Python libraries
#Notes:   To run--> go to directory of this file and type ./python_libraries.sh in command line"

echo "Downloading Python Libraries...."

echo "numpy:----------------------------------"
sudo apt-get install python3-numpy

echo "scikit-learn:----------------------------------"
sudo pip3 install scikit-learn

echo "matplotlib:----------------------------------"
sudo pip3 install matplotlib

echo "scipy:----------------------------------"
sudo apt-get install python3-scipy

echo "beautifulsoup4:----------------------------------"
sudo apt-get install python3-bs4

echo "pandas:---------------------------------"
sudo apt-get install python3-pandas

echo "pandas-datareader:---------------------------------"
sudo pip3 install pandas-datareader

echo "tkinter:--------------------------------"
sudo apt-get install python3-Tk


#END
