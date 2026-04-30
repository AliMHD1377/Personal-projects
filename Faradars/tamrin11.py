# به نام خدا

'''
Calculating income tax following the given laws
'''

income = 45000
print("Given_income:", income)

tax_payable = 0
if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    tax_payable = (income - 10000) * (10 / 100)
else:
    tax_payable = 10000 * (10 / 100)
    
    # remaining 20%tax
    tax_payable += (income - 20000) * (20 / 100)

print("tax_payable=", tax_payable)
