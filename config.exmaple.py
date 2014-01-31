__author__ = 'Daniel Dreier'

## Configuration class
# Example cron entry, every 12 hours on the first minute of the hour:
# 0 */12 * * * python3 /path/to/watcher.py

class Settings:
    # URL to check for changes
    url = "some.website.com/to/check"

    ## Mailing configuration, assumes that the server requires authentication
    # SMTP server address
    mail_server = "mail.example.com"
    # Mail server username
    mail_user = "someone@example.com"
    # Mail server password
    mail_password = "supersecurepassword"
    # Sending email address
    mail_sender = "webwatcher@example.com"
    # Email Recipients
    recipient = "someone@example.com"
