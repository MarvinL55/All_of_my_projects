import smtplib, ssl

port = 465

password = input("Type your password and press enter:")

contex = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=contex) as server:
    server.login("my@gmail.com", password)