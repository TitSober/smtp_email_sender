import smtplib
def send_email(mess,mail):
    password1 = "testmail123"
    email_user = 'testprg001v1@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, password1)


    message = mess
    server.sendmail(email_user, mail, message)
    server.quit()
