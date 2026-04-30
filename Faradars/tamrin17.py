# به نام خدا

'''
Secure one-time password generation
'''

import secrets


otp = secrets.SystemRandom().randrange(100000, 999999)

print("Generating 6 digit random OTP")
print('Secure random OTP is', otp)
