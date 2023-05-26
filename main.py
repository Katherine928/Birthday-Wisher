import datetime as dt
import smtplib

import pandas as pd
import random

today = dt.date.today()
print(today)
today_tuple = (today.month, today.day)
my_email = "katherinebrookstest@gmail.com"
to_email = "katherinebrookstest@yahoo.com"
password = "otrpehlrvkyuyuou"

data = pd.read_csv('birthdays.csv')

birthdays_dict = {
    (data_row['month'], data_row['day']): data_row
    for index, data_row in data.iterrows()
}
print(birthdays_dict)

if today_tuple in birthdays_dict:
    file_path =f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as f:
        content = f.read()
        content = content.replace('[NAME]', birthdays_dict[today_tuple]['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: Happy Birthday {birthdays_dict[today_tuple]['name']}!\n\n{content}"
        )






