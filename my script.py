python
import streamlit as st
st.title("my first stream lit app")
first_name = st.text_input("enter your first name:")
surname = st.text_input("enter your surname:")
st.write("hello", first_name, surname)
age = st.number_input("enter your age:",min_value=5,max_value=85)
# code outside the conditional block
if age >=18:
    st.write("you can provide your id number because you are adult")
elif age >= 13:
    st.write("you are a teenager")
else:
    st.write("you are a child")
    #___code moved outside the conditional block___
id_number = st.text_input("can i have your id number:",min_characters=6,max_characters=10)
st.write("thanks we will protect your information, so dont worry:")
country = st.text_input("which country are you from:")
st.write("ooh you are from", country, "that's so great")