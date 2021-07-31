import pywhatkit as kit


def Whatsapp():
    rec_no = '+91 83101 51688'
    message = 'Covid System Urgent Message'
    delay = 2   # delay in seconds
    browser = 'chrome'
    kit.sendwhatmsg_instantly(rec_no, message, delay, browser, False)


if __name__ == '__main__':
    Whatsapp()
