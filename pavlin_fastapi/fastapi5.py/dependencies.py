import abc

class EmailSender(abc.ABC):
    @abc.abstractmethod
    def send(self, email:str, message:str):
        pass

class SendGridSender(EmailSender):
    def send(self, email:str, message:str):
        print(f'Sending {message} to {email} using SendGridSender')


class MailchimpSender(EmailSender):
    def send(self, email:str, message:str):
        print(f'Sending {message} to {email} using Mailchimp')

def send_email(email:str, message:str, sender: EmailSender):
    sender.send(email,message)


class Sender(object):
    def __init__(self):
        self.email_sender=SendGridSender()

mail_chimp_sender=MailchimpSender()
sendgrid_sender=SendGridSender()
send_email('','', mail_chimp_sender)