#!/usr/bin/python
import time

from Clearing import clear
from DBLogic import CreateTables, NewHospitalCreation_Switch, Read_Switch
from Read import final_report
from Spreadsheet import ReadSheet


def ReadEntry():
    WhatToRead = int(input("What do you want to Read?\n"
                           "1. Number of Beds Available\n"
                           "2. Number of Oxygen Tanks Available\n"))
    Read_Switch(WhatToRead)
    del WhatToRead
    Read = input("Do you want to Read Data? Y / N ")
    clear()
    if Read == 'y' or Read == 'Y':
        ReadEntry()


def DataEntry():
    Switch = int(input("1. Add New Hospital\n"
                       "2. Update Hospital Data\n"))
    NewHospitalCreation_Switch(Switch)
    del Switch
    Data = input("Do you want to enter Data? Y / N ")
    clear()
    if Data == 'y' or Data == 'Y':
        DataEntry()


def Check_User():
    uploads = int(input('Did you upload User''s body data from Sensors? Y / N '))
    if uploads == 'y' or uploads == 'Y':
        ReadSheet()


if __name__ == '__main__':
    CreateTables()
    clear()
    data = input("Do you want to enter data? Y / N ")
    if data == 'y' or data == 'Y':
        DataEntry()
    clear()

    read = input("Do you want to read Data? Y / N ")
    if read == 'y' or read == 'Y':
        final_report()
    time.sleep(5)
    clear()

    check = input("Do you want to Check for Possibility of Covid-19? Y / N ")
    if check == 'y' or check == 'Y':
        Check_User()
    clear()
