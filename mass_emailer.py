import smtplib
import sys
import logging

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email_one(input_email, subject_line):
    #Email Addresses
    sender_email = "######"
    receipient_email = input_email

    #Setting Up Sender and MSG parameters
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject_line
    msg['From'] = sender_email
    msg['To'] = receipient_email

    text = "Hello. Test Email."

    #Input the desired HTML file
    file_name = sys.argv[2]
    html_object = open(file_name, 'r')
    html = html_object.read()

    #MIME in two parts
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    username = "######"
    password = "######"

    server = smtplib.SMTP("smtp.gmail.com:587")
    #server = smtplib.SMTP("localhost:1025")
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(sender_email, receipient_email, msg.as_string())
    server.quit()


def main():
    number_of_emails_sent = 0
    email_subject = raw_input("Subject of Email?: ")

    file_used = open(sys.argv[1], "r")
    emails_list = file_used.read().split()
    log_file = open("email_log_file.txt", "w") #Comment This Out to Print to Command Line. (1)

    for email_address in emails_list:
        #print email_address.lstrip()
        if email_address != '\n':
            email_one(email_address, email_subject)
            number_of_emails_sent = number_of_emails_sent + 1
            log_file.write("%s.....sent\n" % email_address) #Comment This Out to Print to Command Line. (2)
        else:
            pass

    print "Number of Emails Sent: %i" % number_of_emails_sent
    log_file.close() #Comment This Out to Print to Command Line.(3)


if __name__ == "__main__":
    main()
