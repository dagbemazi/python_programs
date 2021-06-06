#! python

import operator
import csv
import re

errors = {}
user_info_count = {}
error_user = {}
usage_stats = {}


def search_errors_info():

    with open('syslog.log') as file:
        for line in file:
            if ' ERROR: ' in line:

                find_error = re.search(
                    r"ticky: ERROR: ([\w ]*) .*\(([\w ]*)\)", line)
                error_description = find_error.group(1)

                if error_description not in errors:
                    errors[error_description] = 1
                else:
                    errors[error_description] += 1

                error_count = find_error.group(2)

                if error_count not in error_user:
                    error_user[error_count] = 1
                else:
                    error_user[error_count] += 1

            elif ' INFO: ' in line:
                find_user = re.search(r'ticky: INFO: .*\(([\w ]*)\)', line)
                res = find_user.group(1)
                if res not in user_info_count:
                    user_info_count[res] = 1
                else:
                    user_info_count[res] += 1
    file.close()


def combine_data():

    list_of_dicts = [user_info_count, error_user]

    for user in user_info_count.keys():
        usage_stats[user] = tuple(usage_stats[user]
                                  for usage_stats in list_of_dicts)


def write_error_csv():
    sorted_dict = dict(
        sorted(errors.items(), key=operator.itemgetter(1), reverse=True))

    with open("errors.csv", 'w', newline="") as error:
        field_names = ["Errors", "Count"]
        writer = csv.DictWriter(error, fieldnames=field_names)
        writer.writeheader()

        for key, value in sorted_dict.items():
            row_data = {"Errors": key, "Count": value}
            writer.writerow(row_data)


def write_usage_stats():

    with open("stats.csv", "w", newline="") as stats:
        field_names = ["USER", "INFO", "ERROR"]
        writer = csv.DictWriter(stats, fieldnames=field_names)
        writer.writeheader()

        for key, value in usage_stats.items():
            info, error = value
            csv_row_data = {"USER": key, "INFO": info, "ERROR": error}
            writer.writerow(csv_row_data)


if __name__ == "__main__":
    search_errors_info()
    combine_data()
    write_usage_stats()
    write_error_csv()
