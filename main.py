from datetime import datetime
import pandas as pd
import random
import smtplib

# Constants
EMAIL = "udemytestmail1@gmail.com"
PASSWORD = "ynmk ncal ghzo ocmu"


def send_birthday_email(to_email, name, contents):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        message = f"Subject: Happy Birthday!!\n\n{contents}"
        connection.sendmail(from_addr=EMAIL, to_addrs=to_email, msg=message)


def main():
    today = (datetime.now().month, datetime.now().day)

    # Read CSV data
    data = pd.read_csv("birthdays.csv")
    bday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

    if today in bday_dict:
        birthday_person = bday_dict[today]
        file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

        try:
            with open(file_path) as letter_file:
                contents = letter_file.read()
                contents = contents.replace("[NAME]", birthday_person["name"])

            send_birthday_email(birthday_person["email"], birthday_person["name"], contents)

        except FileNotFoundError:
            print(f"Error: The file {file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
