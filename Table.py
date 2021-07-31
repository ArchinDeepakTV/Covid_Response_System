#!/usr/bin/python

import psycopg2

from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE hospitals (
            hospital_id INT PRIMARY KEY UNIQUE,
            hospital_name VARCHAR(255),
            mail_id VARCHAR(255),
            distance INT,
            oxy_tanks INT,
            beds INT
        )
        """,
        """
        CREATE TABLE kin (
            mail_id VARCHAR(255) UNIQUE NOT NULL,
            kin_name VARCHAR(255)
        )
        """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table NewHospitalCreation_Switch_one by NewHospitalCreation_Switch_one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
