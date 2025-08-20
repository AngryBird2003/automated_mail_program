import random
import smtplib
import datetime as dt
import pandas as pd
import os


# with open("quotes.txt", "r") as file:
#     quotes = file.readlines()

# check_day = "Monday"
# day = dt.datetime.now()
# if day.weekday() == 0:
#     random_quote = random.choice(quotes)
# date_today = dt.datetime(year=now.year, month=now.month, day=now.day)


username = "uvcodetest@gmail.com"
password = "dtbs fdlb vqec haqj"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=username, password=password)

dataframe = pd.read_csv("birthdays.csv")
now = dt.datetime.now()

names = []
emails = []
letter_files = os.listdir("letter_templates")

for index, value in dataframe.iterrows():
    if value["month"] == now.month and value["day"] == now.day:
        names.append(value["name"])
        emails.append(value["email"])

# sending email for every name having birthday
for x in names:
    email = emails[names.index(x)]
    letter_file = random.choice(letter_files)
    with open(f"letter_templates/{letter_file}", "r") as file:
        content = file.read()
        content = content.replace("[NAME]", x)
        content = content.replace("Angela", "Yuvraj")
        connection.sendmail(from_addr=username, to_addrs=email, msg=f"Subject:Happy Birthday!\n\n"
                                                                    f"{content}")

connection.close()


