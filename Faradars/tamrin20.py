# به نام خدا

'''
Subtracting one week from the given date
'''

from datetime import datetime, timedelta


given_date = datetime(2020, 2, 25)
print("Given date:", given_date)

res_date = given_date - timedelta(days=7)
print("New date:", res_date)
