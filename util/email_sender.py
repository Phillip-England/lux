import smtplib

def email_sender(options):

  email = options['email']
  password = options['password']
  message = options['message']
  send_to = options['send_to']
  subject = options['subject']

  smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
  smtpObj.ehlo()
  smtpObj.starttls()
  smtpObj.login(email, password)
  smtpObj.sendmail(email, send_to, f'Subject: {subject}\n\n {message}')
  smtpObj.quit()
