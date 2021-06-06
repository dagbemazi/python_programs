#! python
#! /usr/bin /env python3

import random
import datetime


msg_type = ["INFO", 'ERROR']

usernames = ['james', 'mcintosh', 'hayle', 'fsusan',
             'greg', 'hayden', 'fentuo', 'sysadmin', 'fblay']
descriptions = ['Created ticket', 'Failed to connect to DB',
                'Service timeout', 'Bad input']
date = datetime.date.today()

# Generate pseudo syslog.log to use to test clean_ticky.log
with open("syslog.log", 'w') as logfile:
    for user in usernames:
        for msg in msg_type:
            for description in descriptions:
                numbers = random.randint(1000, 4000)
                logfile.write(
                    f"{date} Ubuntu debian server ticky: {msg}: {description} [#{numbers}] ({user})\n")
