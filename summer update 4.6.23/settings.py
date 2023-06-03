import os

PATH_STATIC = os.path.dirname(__file__) + os.sep + "static" + os.sep # get folder where this file is   # os.sep get right separator \ or /
PATH_INSTANCE = os.path.dirname(__file__) + os.sep + "instance" + os.sep 
# C:\Users\romak\Downloads\main project\flask-main\28.5.23\instance\ =  directory PATH_INSTANCE
# C:\Users\romak\Downloads\main project\flask-main\28.5.23\static\ =  directory PATH_STATIC

# this file should not be uploaded on the GitHub ( contains secret keys, passwords )
