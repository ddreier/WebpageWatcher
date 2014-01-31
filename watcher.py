__author__ = 'Daniel Dreier'

import urllib.request
import hashlib
import pickle
import smtplib
from email.mime.text import MIMEText
from config import Settings


def main():
    with urllib.request.urlopen(Settings.url) as url:
        s = url.read()
    h = hashlib.sha256(s).hexdigest()
    print(h)
    try:
        f = open("hash", "rb+")
        print("file exists, loading hash")
        hash_from_file = pickle.load(f)
        if hash_from_file == h:
            print("same")
        else:
            print("different, emailing and dumping new hash")
            f.seek(0)
            pickle.dump(h, f)
            send_mail(Settings.url)
    except IOError:
        f = open("hash", "wb+")
        print("file didn't exist, dumping hash")
        pickle.dump(h, f)
    f.close()


def send_mail(url):
    message = MIMEText("The webpage %s has changed since last checked" % url)

    server = Settings.mail_server
    user = Settings.mail_user
    password = Settings.mail_password

    recipient = Settings.recipient
    sender = Settings.mail_sender
    message['Subject'] = "WebsiteWatcher Alert"
    message['From'] = sender
    message['To'] = recipient

    session = smtplib.SMTP(server)
    session.login(user, password)
    session.sendmail(sender, [recipient], message.as_string())

    session.quit()

if __name__ == "__main__":
    main()
