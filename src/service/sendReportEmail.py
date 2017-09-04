import smtplib
from os.path import basename
from email.mime.text import MIMEText
from models.emailObject import EmailObject
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate
from email.mime.application import MIMEApplication


class SendReportEmail(object):

    def __init__(self, email):
        if isinstance(email, EmailObject):
            self.send_email(email.get_sender(), email.get_recipient(), email.get_subject(), email.get_body(),
                            email.get_files(), email.get_server())
        else:
            print 'Incorrect email object given'
            exit(1)

    def send_email(self, send_from, send_to, subject, text, files=None,
                   server="smtp.gmail.com:587"):
        assert isinstance(send_to, list)

        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(text))

        for attached_file in files or []:
            with open(attached_file, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(attached_file)
                )
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(attached_file)
                msg.attach(part)

        smtp_server = smtplib.SMTP(server)
        smtp_server.starttls()
        smtp_server.login("test_username", "test_security_token")
        smtp_server.sendmail(send_from, send_to, msg.as_string())
        smtp_server.close()
