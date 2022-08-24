import smtplib


gmail_user = 'raspberrypigroup2@gmail.com'
gmail_password = 'tvrspwcfqyzjuhzh'

sent_from = gmail_user
to = ['almoglevi1008@gmail.com']
subject = 'Alert!! Grandparent has been abused'
body = 'Your grandparent has been abused.' \
       'Please go back home in next minute.' \
       'If not we will contact the police!'

email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

except:
    print('Something went wrong...')
