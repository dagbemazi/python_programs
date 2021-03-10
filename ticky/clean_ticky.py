#! python

import operator
import csv
import re



#per_usage_stats = {}
errors = {}
user_info_count = {}
error_user = {}


def search():
    with open('syslog.log') as file:
        for line in file:
            if ' ERROR: ' in line:
                find_error = re.search(r"ticky: ERROR: ([\w ]*) .*\(([\w ]*)\)", line)
                answer = find_error.group(1)
                if answer not in errors:
                    errors[answer] = 1
                else:
                    errors[answer] += 1
                error_count = find_error.group(2)
                if error_count not in error_user:
                    error_user[error_count] = 1
                else:
                    error_user[error_count] += 1
                
search()
hi = dict(sorted(errors.items(), key=operator.itemgetter(1), reverse=True))



def search_info_count():
    with open('syslog.log') as infos:
        for line in infos:
            if ' INFO: ' in line:
                find_user = re.search(r'ticky: INFO: .*\(([\w ]*)\)', line)
                res = find_user.group(1)
                if res not in user_info_count:
                    user_info_count[res] = 1
                else:
                    user_info_count[res] += 1


combined = {}
def main():
    search_info_count()
    search()
    total = [user_info_count, error_user]

    for k in user_info_count.keys():
        combined[k] = tuple(combined[k] for combined in total)


main()



def write_error_csv():
    with open("errors.csv", 'w', newline="") as error:
        fieldnames = ["Errors", "Count"]
        writer = csv.DictWriter(error, fieldnames=fieldnames)

        writer.writeheader()

        for key, value in hi.items():
            h = {"Errors": key, "Count": value}
            writer.writerow(h)


write_error_csv()


def write_usage_stats():
    with open("stats.csv", "w", newline="") as stats:
        fieldnames = ["USER", "INFO", "ERROR"]

        writer = csv.DictWriter(stats, fieldnames=fieldnames)
        writer.writeheader()


        for key, value in combined.items():
            info, error = value
            e = {"USER": key, "INFO": info, "ERROR": error}
            writer.writerow(e)

write_usage_stats()