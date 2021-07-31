# Function to read the contacts from a given contact file and return a
# list of names and email addresses
# import necessary packages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template


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


def mails():
    gmail_id = "1rn18ec022.archindeepak@gmail.com"
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmail_id, "@rch1n2203")

    names, emails = get_contacts('kin_contacts.txt')  # read contacts
    message_template = read_template('healthy_message.txt')

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message
        msg['From'] = gmail_id
        msg['To'] = email
        msg['Subject'] = "Covid System"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
        print("DONE")

        del msg


if __name__ == '__main__':
    mails()
