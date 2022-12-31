import imaplib
import smtplib

def email_sender(options):

  email = options['email']
  password = options['password']
  message = options['message']
  send_to = options['send_to']
  subject = options['subject']

