import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email():
    # Email and password (you may need to enable less secure apps in your Gmail settings)
    gmail_address = "thebryanniwa@gmail.com"
    gmail_password = "mirv dnht ywul yuwg"

    # Email content
    subject = "Dune Tickets"
    body = "Go buy those tickets!"
    to_email = "thebryanniwa@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart()
    msg["From"] = gmail_address
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach body of email
    msg.attach(MIMEText(body, "plain"))

    # Establish connection to Gmail's SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    # Login to Gmail
    server.login(gmail_address, gmail_password)

    # Send email
    text = msg.as_string()
    server.sendmail(gmail_address, to_email, text)

    # Close connection
    server.quit()

    print("Email sent successfully to", to_email)
