__author__ = 'Daniel Dreier'

import urllib.request
import hashlib
import pickle
import smtplib


def main():
    page_url = "http://www.google.com"
    with urllib.request.urlopen(page_url) as url:
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
            send_mail(page_url)
    except IOError:
        f = open("hash", "wb+")
        print("file didn't exist, dumping hash")
        pickle.dump(h, f)
    f.close()


def send_mail(url):
    server = "mail.server.com"
    user = "username"
    password = "super_strong_password"

    recipients = ["me@email.com"]
    sender = "script@email.com"
    message = "The webpage " + url + " has changed since last checked"

    session = smtplib.SMTP(server)
    session.login(user, password)
    session.sendmail(sender, recipients, message)


if __name__ == "__main__":
    main()
