import re

def process_date(this_date):
    if not re.search(r'^\d\d\d\d-\d\d-\d\d$', this_date):
        raise ValueError("please submit date in YYYY-MM-DD format")

    print(f"the submitted date is {this_date}")

process_date("1980-01-08")
print()
process_date("1/3/1980")
