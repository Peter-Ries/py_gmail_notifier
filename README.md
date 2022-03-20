# py_gmail_notifier

Small script to check a gmail account for new mails.

It was scripted due to plasmoid-ultimate-gmail-feed (https://github.com/Intika-KDE-Plasmoids/plasmoid-ultimate-gmail-feed) stopped working for me.

Currently it supports one gmail account. It either returns the number of unread mails as a string or a list of "sender - subject" for all unread mails. I use it with "Command Output" (https://github.com/Zren/plasma-applet-commandoutput) plasmoid to print the string in KDEs taskbar.

The script requires a minimal config file _~/.config/py_gmail_notifier.cfg_ with:

```
[account]
username = your_login_user
password = your_login_password # app password when 2FA is activated
```

Supported arguments are:

```
py_gmail_notifier.py - allowed arguments:
        -c      unread email count
        -d      debug: show JSON output

everything else returns list of "(sender) - summary"
```
