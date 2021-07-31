import smtplib

import COVID19Py


def LiveTracking():
    gmail_id = "1rn18ec022.archindeepak@gmail.com"

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(gmail_id, "@rch1n2203")

    # message to be sent
    covid19 = COVID19Py.COVID19(data_source="csbs")
    latest = covid19.getLatest()
    message = "Total Number of cases in the World \n" + str(latest)

    mail = ["archindeepakad.ad@gmail.com", "aporwal2207@gmail.com", "aryanarora0106@gmail.com"]

    # sending the mail
    for i in range(0, len(mail)):
        s.sendmail("1rn18ec022.archindeepak@gmail.com", mail[i], message)
        print('done ' + str(i + 1))

    # terminating the session
    s.quit()


if __name__ == '__main__':
    LiveTracking()
