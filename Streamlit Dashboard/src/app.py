# به نام خدا

import streamlit as st
from password_generator import PinCodeGenerator, MemorablePasswordGenerator, RandomPasswordGenerator


st.image("src/images/91kmT1yHUsL.png", width=500)
st.title(':closed_lock_with_key: Password Generator')

option = st.radio(
    "نوع رمز عبور را انتخاب کنید :",
    ("Pin Code", "Random Password", "Memorable Password")
)

if option == 'Pin Code':
    length = st.slider("طول کد پین را انتخاب کنید", 4, 20)
    generator = PinCodeGenerator(length)
elif option == 'Random Password':
    length = st.slider("طول کد پین را انتخاب کنید", 4, 20)
    numbers = st.toggle("شامل اعداد باشد")
    symbols = st.toggle("شامل نمادها باشد")
    generator = RandomPasswordGenerator(length, numbers, symbols)
elif option == 'Memorable Password':
    num_of_words = st.slider("طول کلمات را انتخاب کنید", 2, 10)
    separator = st.text_input('separator', value='-')
    capitaliz = st.toggle("Capitalize")
    generator = MemorablePasswordGenerator(num_of_words, separator, capitaliz)

password = generator.generate()
st.write("رمز عبور شما :")
st.header(fr"``` {password} ```")
