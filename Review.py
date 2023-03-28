from smtplib import SMTP
from imaplib import IMAP4_SSL
from email import message_from_string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class WorkingWithMail:
    def __init__(self):
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"

    def send_message(self, login, password, subject, recipients, message):
        self.message = MIMEMultipart()
        self.message['From'] = login
        self.message['To'] = ', '.join(recipients)
        self.message['Subject'] = subject
        self.message.attach(MIMEText(message))

        self.message_send = SMTP(self.gmail_smtp, 587)
        self.message_send.ehlo()
        self.message_send.starttls()
        self.message_send.ehlo()
        self.message_send.login(login, password)
        self.message_send.sendmail(login, self.message_send, self.message.as_string())
        self.message_send.quit()

    def recieve_message(self, login, password, header=None):
        mail = IMAP4_SSL(self.gmail_imap)
        mail.login(login, password)
        mail.list()
        mail.select()
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        message_from_string(raw_email)
        mail.logout()

if __name__ == '__main__':
    sending = WorkingWithMail()
    sending.send_message('login@gmail.com', 'qwerty', 'Subject',
                         ['vasya@email.com', 'petya@email.com'], 'Message')
    sending.recieve_message('login@gmail.com', 'qwerty')
