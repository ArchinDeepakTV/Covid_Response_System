import os
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from Clearing import clear

gmail_id = os.environ.get('SENDER_EMAIL')
gmail_password = os.environ.get('SENDER_EMAIL_PASSWORD')


def MailOption(ID1, H1, ID2, H2, ID3, H3, ID4, H4, ID5, H5, temperature, spo2, pulse_rate):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # s.starttls()
    s.login(gmail_id, gmail_password)

    # read contacts
    names, emails = get_contacts('kin_contacts.txt')
    message_template = read_template('MailUser.txt')

    print("Sending Mails")
    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add in the name of the receiver to the message template
        # add the medical details of patient to the message template
        message = message_template.substitute(PERSON_NAME=name.title(), TEMP=temperature, SPO2=spo2,
                                              PULSE_RATE=pulse_rate, H_1=H1.upper(), H_2=H2.upper(),
                                              H_3=H3.upper(), H_4=H4.upper(), H_5=H5.upper(),
                                              ID_1=ID1, ID_2=ID2, ID_3=ID3, ID_4=ID4, ID_5=ID5)

        # setup the parameters of the message
        msg['From'] = gmail_id
        msg['To'] = email
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


def mail_healthy():
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # s.starttls()
    s.login(gmail_id, gmail_password)

    # read contacts
    names, emails = get_contacts('kin_contacts.txt')
    message_template = read_template('healthy_message.txt')

    print("Sending Mails")
    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add in the name of the receiver to the message template
        # add the medical details of patient to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message
        msg['From'] = gmail_id
        msg['To'] = email
        msg['Subject'] = "COVID SYSTEM"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        print("DONE")
    clear()
    print('Sending Mails COMPLETED \n\n EXITING PROGRAM')
    time.sleep(1)
    clear()


def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)
