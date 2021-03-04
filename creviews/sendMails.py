import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail_reset_password(send_to, reset_password):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("alisherkamal13101@gmail.com", "ALIsher2001")
    message = MIMEMultipart()
    message["From"] = "alisherkamal13101@gmail.com"
    message["To"] = send_to
    message["Subject"] = "[CReview] Your password was reset"
    body = 'Hello \n' + 'We wanted to let you know that your CReview User Account password was reset.\n Your new password is ' + reset_password + '\n' + 'If you run into problems, please contact support by visiting CReview/ContactUS ' + '\n' + 'Please do not reply to this email with your password. We will never ask for your password, and we strongly discourage you from sharing it with anyone.'
    message.attach(MIMEText(body, "plain"))
    text = message.as_string()
    s.sendmail("sender_email_id", send_to, text)
    s.quit()


def send_complain_mail(first_name, full_name, email, subject, message_send):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("alisherkamal13101@gmail.com", "ALIsher2001")
    message = MIMEMultipart()
    message["From"] = "alisherkamal13101@gmail.com"
    message["To"] = "CReview"
    message["Subject"] = subject
    body = 'From : ' + full_name + '\n' + 'Email : ' + email + '\n' + 'Subject : ' + subject + '\n' + 'Message : ' + message_send + '.'
    message.attach(MIMEText(body, "plain"))
    text = message.as_string()
    s.sendmail("sender_email_id", "alisherkamal13101@gmail.com", text)
    s.quit()


def generate_password():
    import random
    # Importing string library function
    import string

    def rand_pass(size):
        # Takes random choices from
        # ascii_letters and digits
        generate_pass = ''.join([random.choice(string.ascii_uppercase +
                                               string.ascii_lowercase +
                                               string.digits +
                                               string.ascii_lowercase +
                                               string.digits)
                                 for n in range(size)])

        return generate_pass

        # Driver Code

    password = rand_pass(8)
    return password
