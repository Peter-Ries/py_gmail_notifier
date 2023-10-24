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

## Installation

Assuming you have a working python3 on your system you additionally might need following modules:

```
pip install urllib3
pip install configparser
pip install xmltodict
pip install json
```

### Config file

Save the sample file with your settings to _~/.config/py_gmail_notifier.cfg_

Usually you have your gmail account set up with a 2FA. So you need to create an application password in your google account security settings.

## Example to create a "taskbar plasmoid"

- configure py_gmail_notifier.cfg
- place python script in your bin directory
- test output and connection first by calling _python yourpathhere/py_gmail_notifier.py -C_ - you should get a number of unread mails
- take sample script _mailplasmoid.sh_
- install MesloLGS NF font
- install plasmoid _commandoutput_ (https://store.kde.org/p/1166510/)
- use plasmoid and configure it to call mailplasmoid.sh 
  - use interval e. g. 60000 ms (with wait for completion)
  - use MesloLGS NF font with 22px
  - optionally adjust color if using a light taskbar. breeze dark should use #fcfcfc and outline #232629
  - fixed width 26px works great
  - run command (if you configured mailbox in chrome): _google-chrome-stable https://mail.google.com/mail/u/0/#inbox_
  
That's it. You should now have a mailenvleope icon in your taskbar that changes whenever there's new mail. When you clock on that icon chrome will open your inbox

## Disclaimer

This script is provided without any guarantee to work for you, nor will I give support. I wrote it for my use case and you might copy/share/modify as you like. :)
