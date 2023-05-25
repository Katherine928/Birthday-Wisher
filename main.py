# import smtplib
#
# my_email = "katherinebrookstest@gmail.com"
# password = "otrpehlrvkyuyuou"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="katherinebrookstest@yahoo.com",
#                         msg="Subject:Hello\n\nThis is a test email")
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
