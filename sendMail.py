import smtplib, ssl


# Change the variables below according to your queries

port = 465  # For SSL protocol
smtp_server = "gmail.com"  #ex. smtp_server
sender_email = "sender@@gmail.com"  # Enter your address
receiver_email = "example@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

