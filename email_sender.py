import smtplib
from email.message import EmailMessage
import ssl

sender_email = 'ozodbek.rajabboyev8555@gmail.com'
sender_password = 'kjwmlamrngcykwow'
recipient_email = 'ozodbek2625@gmail.com'
subject = 'Hello from Ozodbek Rajabboyev'
message = 'This is second test email sent from Python.'

em = EmailMessage()
em['From'] = sender_email
em['To'] = recipient_email
em['Subject'] = subject
em.set_content(message)


context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.sendmail(sender_email, recipient_email, em.as_string())
    print("Email sent succesfully!")
except smtplib.SMTPException as e:
        print('Error sending email:', e)
