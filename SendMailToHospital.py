# import necessary packages
import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from Clearing import clear

gmail_id = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('SENDER_EMAIL_PASSWORD')


def mail_hospitals(temperature, spo2, pulse_rate, emails):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # s.starttls()
    s.login(gmail_id, gmail_password)

    # read contacts
    message_template = read_template('hospital_message.txt')

    print("Sending Mails")
    # For each contact, send the email:
    msg = MIMEMultipart()  # create a message

    # add in the name of the receiver to the message template
    # add the medical details of patient to the message template
    message = message_template.substitute(PERSON_NAME=emails, TEMP=temperature, SPO2=spo2,
                                          PULSE_RATE=pulse_rate)

    # setup the parameters of the message
    msg['From'] = gmail_id
    # msg['To'] = emails
    msg['To'] = 'archindeepakad.ad@gmail.com'
    msg['Subject'] = "COVID SYSTEM"

    # add in the message body
    msg.attach(MIMEText(message, 'html'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    print("DONE")

    del msg
    clear()
    print('Sending Mails COMPLETED \n\n EXITING PROGRAM')
    time.sleep(1)
    clear()


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


if __name__ == '__main__':
    mail_hospitals(10, 10, 10, 'archindeepakad.ad')
