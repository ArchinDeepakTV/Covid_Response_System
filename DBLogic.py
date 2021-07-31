from Clearing import clear
from Insert import insert_hospitals
from Random import random_id
from Read import read_hospital_one, read_hospital_two
from SearchDB import read_hospital_ID
from Table import create_tables
from Update import update_hospital, update_beds, update_oxygen, update_distance, update_mail


def CreateTables():
    # for creating 2 tables for the user
    create_tables()


def UniqueID():
    # inputting Hospital Unique ID
    # NOTE: : : : We can randomize to get a number and check whether it is already present in the database.
    # If it's present, randomize again until we get a unique number.
    # And when we get a unique number, we fix that number for a hospital.
    ID = int(random_id() * 100000)
    already_exists = read_hospital_ID(ID)
    if already_exists == -1:
        UniqueID()
    insert_hospitals(ID)
    clear()
    Name(ID)


def Name(ID):
    # inputting Name of Hospital
    hospital_name = input("Enter Name of Hospital : ")
    update_hospital(ID, hospital_name)
    MailID(ID)


def MailID(ID):
    mail_id = input('Enter the Mail ID of the Hospital : ')
    update_mail(ID, mail_id)
    Distance(ID)


def Distance(ID):
    # inputting Distance from User
    distance = input("Enter Distance from User ( in km) : ")
    update_distance(ID, distance)
    choice = input("Do you want to input number of oxygen cylinders available? Y / N  ")
    if choice == 'y' or choice == 'Y':
        del choice
        Oxygen(ID, 1)
    else:
        print("Updated \n\n")


def Oxygen(ID, flag):
    # inputting Number of Oxygen Cylinders Available
    oxygen = input("Enter Number of Oxy Tanks available ( in whole numbers) : ")
    update_oxygen(ID, oxygen)
    if flag == 1:
        choice = input("Do you want to input number of beds available? Y / N  ")
        if choice == 'y' or choice == 'Y':
            del choice
            Beds(ID)
    else:
        print("Updated \n\n")


def Beds(ID):
    # inputting Number of Beds available
    beds = input("Enter Number of Beds available ( in whole numbers) : ")
    update_beds(ID, beds)
    clear()
    print("Updated \n\n")


def NewHospitalCreation_Switch_one():
    # for entering details of new hospital
    UniqueID()


def NewHospitalCreation_Switch_two():
    # switch function for updating data
    hospital_data = int(input("Which data to Update?\n"
                              "1. Number of Beds Available\n"
                              "2. Number of Oxygen Cylinders available  "))
    ID = int(input('Enter Hospital ID: '))
    BedsOxygenUpdater_Switch(hospital_data, ID)


def NewHospitalCreation_Switch(argument):
    # switch function using if elif else
    if argument == 1:
        NewHospitalCreation_Switch_one()
    elif argument == 2:
        NewHospitalCreation_Switch_two()
    else:
        print("Invalid Selection")


def BedsOxygenUpdater_Switch_one(ID):
    # for updating number of free beds available in a particular hospital
    Beds(ID)


def BedsOxygenUpdater_Switch_two(ID):
    #  for updating number of oxygen cylinders available in a particular hospital
    Oxygen(ID, 2)


def BedsOxygenUpdater_Switch(argument, ID):
    # switch function using if elif else
    if argument == 1:
        BedsOxygenUpdater_Switch_one(ID)
    elif argument == 2:
        BedsOxygenUpdater_Switch_two(ID)
    else:
        print("Invalid Selection")


def Read_Switch(argument):
    # switch function
    if argument == 1:
        Read_Switch_one()
    elif argument == 2:
        Read_Switch_two()
    else:
        print("Invalid Selection")


def Read_Switch_one():
    #  for reading number of beds available in a particular hospital
    ID = int(input("Enter Hospital ID: "))
    a = read_hospital_one(ID)
    print(a)


def Read_Switch_two():
    #  for Reading number of oxygen tanks available at a particular hospital
    ID = int(input("Enter Hospital ID: "))
    a = read_hospital_two(ID)
    print(a)
