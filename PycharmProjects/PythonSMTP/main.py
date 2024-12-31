import smtplib
#

import datetime as dt
import random

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(day_of_week)
date_of_birth = dt.datetime(year=1980, month=8, day=1)


# print(type(year))
# print(date_of_birth)
def get_quote(filename, line_number):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines[line_number - 1]


def sendemail(quote):
    FROM_ADDR = "wishbirthdayapp@gmail.com"
    PASSWORD = "ndrictijkqvzhrrq"
    TO_ADDR = "kunj281218@yahoo.com"
    #
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=FROM_ADDR, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_ADDR,
            to_addrs=TO_ADDR,
            msg="Subject:Quote of the day\n\n"+ quote
        )


# Usage


if day_of_week == 0:
    quote_of_day = get_quote('quotes.txt', random.randint(0, 101))  # Get the 5th line
    sendemail(quote_of_day)
