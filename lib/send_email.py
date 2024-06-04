import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Emailer:
    __slots__ = ["gmail_address", "gmail_password"]

    def __init__(self, gmail_address, gmail_password):
        self.gmail_address = gmail_address
        self.gmail_password = gmail_password

    def send_success_email(self):
        self.send_email("Movie Tickets", "Your tickets are available. Go get them!")

    def send_error_email(self, error_message):
        self.send_email("Movie Script Error", error_message)

    def send_email(self, subject, body):
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart()
        msg["From"] = self.gmail_address
        msg["To"] = self.gmail_address
        msg["Subject"] = subject

        # Attach body of email
        msg.attach(MIMEText(body, "plain"))

        # Establish connection to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to Gmail
        server.login(self.gmail_address, self.gmail_password)

        # Send email
        text = msg.as_string()
        server.sendmail(self.gmail_address, self.gmail_address, text)

        # Close connection
        server.quit()
