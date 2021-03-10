#! python

import random
import datetime


errors = ["INFO", 'ERROR']
usernames = ['james', 'mcintosh', 'hayle', 'fsusan', 'greg', 'hayden', 'fentuo', 'sysadmin', 'fblay']
description = ['Created ticket', 'Failed to connect to DB', 'Service timeout', 'Bad input']
date = datetime.date.today()
# grap errors from syslog

with open("syslog.log", 'w') as logfile:
    for user in usernames:
        for error in errors:
            for info in description:
                numbers = random.randint(1000, 4000)
                logfile.write(f"{date} Ubuntu debian server ticky: {error}: {info} [#{numbers}] ({user})\n")
