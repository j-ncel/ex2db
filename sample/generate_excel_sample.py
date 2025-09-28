import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta


def generate_excel_sample(filename="sample/sample_data.xlsx", num_rows=100):
    fake = Faker()
    data = {
        "ID": [],
        "Name": [],
        "Last Name": [],
        "Age": [],
        "Gender": [],
        "Height": [],
        "Weight": [],
        "Email": [],
        "Join Date": [],
        "Salary": [],
        "Is Active": []
    }

    for i in range(1, num_rows + 1):
        profile = fake.simple_profile()
        full_name = profile["name"].split()
        first_name = full_name[0]
        last_name = full_name[-1]
        gender = profile["sex"]
        join_date = fake.date_between(start_date="-5y", end_date="today")
        salary = round(random.uniform(25000, 120000), 2)
        is_active = random.choice([True, False])

        data["ID"].append(i)
        data["Name"].append(first_name)
        data["Last Name"].append(last_name)
        data["Gender"].append("Male" if gender == "M" else "Female")
        data["Age"].append(random.randint(18, 65))
        data["Height"].append(round(random.uniform(150.0, 190.0), 1))
        data["Weight"].append(round(random.uniform(50.0, 100.0), 1))
        data["Email"].append(profile["mail"])
        data["Join Date"].append(join_date)
        data["Salary"].append(salary)
        data["Is Active"].append(is_active)

    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Sample Excel file created: {filename} with {num_rows} rows")


if __name__ == "__main__":
    generate_excel_sample()
