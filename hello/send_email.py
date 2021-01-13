import smtplib
 
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

sender_email = 'azadsingh42878@gmail.com' 
password = 'azad@#12345'

server.login(sender_email, password)

receiver_email = input('Enter Receiver Email Address : ')
message_to_send = input('Enter your Message : ')

server.sendmail(sender_email, receiver_email, message_to_send)

server.quit()