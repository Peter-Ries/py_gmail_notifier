import os
import sys
import urllib3
import json
import xmltodict
from configparser import ConfigParser

#
#   ### global variables ###
script_name = os.path.basename(__file__)
user_home = os.path.expanduser("~")
config_file = os.path.expanduser(
    f"{user_home}/.config/{os.path.splitext(script_name)[0]}.cfg"
)


#
#   ### fetch the gmail atom feed and prepare it as a JSON ###
def read_config(config_file):

    try:
        config = ConfigParser()
        config.read(config_file)
        g_user = config["account"]["username"]
        g_password = config["account"]["password"]

        return g_user, g_password

    except Exception as e:
        print(f"ERROR - {e}")
        print(f"\nConfig file needs to be '{config_file}'")
        print("\nFormat of config file:")
        print("\t[account]")
        print("\tusername = your_login_user")
        print("\tpassword = your_login_password # app password when 2FA is activated\n")

        return "ERROR", "ERROR"


#
#   ### fetch the gmail atom feed and prepare it as a JSON ###
def get_feed(g_url, g_user, g_password):

    try:
        http = urllib3.PoolManager()
        headers = urllib3.make_headers(basic_auth=f"{g_user}:{g_password}")
        xml = http.request("GET", g_url, headers=headers)
        feed_as_json = json.loads(json.dumps(xmltodict.parse(xml.data)))
        return feed_as_json

    except Exception as e:
        print(f"ERROR - {e}")
        return "ERROR"


#
#   ### MAIN ###
if __name__ == "__main__":

    #
    # google stuff
    g_url = "https://mail.google.com/mail/feed/atom"
    g_user, g_password = read_config(
        config_file
    )  # when 2FA provide your application specifc passwordpassword!

    if g_user != "ERROR" and g_password != "ERROR":
        feed = get_feed(g_url, g_user, g_password)

        try:
            if feed != "ERROR":

                # get unread mail count here as we need it several times
                unread_mails = int(feed["feed"]["fullcount"])

                # do we have cmd line arguments?
                if len(sys.argv) > 1:

                    # -c - just print unread emails count
                    if str(sys.argv[1]) == "-c":

                        # better output string ;)
                        if unread_mails == 1:
                            print(f"{unread_mails} unread email")
                        else:
                            print(f"{unread_mails} unread emails")

                    # -d - print complete JSON to debug stuff
                    elif str(sys.argv[1]) == "-d":
                        print(f"config filepath:\t{config_file}")
                        print(f"google feed url:\t{g_url}")
                        print(f"google username:\t{g_user}")
                        print(f"google password:\t{g_password}")
                        print(f"feed:\n\t{feed}\n\n")

                    # unknown argument? then print allowed arguments
                    else:
                        print(
                            f"\n{script_name} - allowed arguments:\n\t-c\tunread email count\n\t-d\tdebug: show JSON output"
                        )

                # anything else - print email-sender and email-subject of all emails
                else:

                    entries = feed["feed"]["entry"]

                    # if only one entry we dont have a list, then just print. Otherwise loop...
                    if unread_mails == 0:
                        print("0 unread mails")
                    if unread_mails == 1:
                        print(f"({entries['author']['name']}) - {entries['title']}")
                    else:
                        for index in range(0, unread_mails):
                            print(
                                f"({entries[index]['author']['name']}) - {entries[index]['title']}"
                            )

            else:
                print(feed)

        except Exception as e:
            print(f"ERROR - {e}")
