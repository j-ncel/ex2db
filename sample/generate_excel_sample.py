import pandas as pd
from faker import Faker
import random


def generate_excel_sample(filename="sample/sample_data.xlsx", num_rows=100):
    fake = Faker()
    data = {
        "Name": [],
        "Last Name": [],
        "Age": [],
        "Gender": [],
        "Height": [],
        "Weight": []
    }

    for _ in range(num_rows):
        profile = fake.simple_profile()
        full_name = profile["name"].split()
        first_name = full_name[0]
        last_name = full_name[-1]
        gender = profile["sex"]

        data["Name"].append(first_name)
        data["Last Name"].append(last_name)
        data["Gender"].append("Male" if gender == "M" else "Female")
        data["Age"].append(random.randint(18, 65))
        data["Height"].append(round(random.uniform(150.0, 190.0), 1))
        data["Weight"].append(round(random.uniform(50.0, 100.0), 1))

    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
    print(f"Sample Excel file created: {filename} with {num_rows} rows")


if __name__ == "__main__":
    generate_excel_sample()
