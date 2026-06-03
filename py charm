from tkinter import Menu

import streamlit as st
import pandas as pd
from datetime import datetime
import uuid
from pathlib import path

st.set_page_config(page_title="kurungu united club registration", page_icon=":soccer:", layout="centered")
st.title("kurungu united club registration")
st.write("welcome to kurungu united club registration form. please fill in the details below to register as a member of our club")

DATA_FILE =path("members.csv")

def load_data():
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    return pd.dataframe(colums=["full_name", "position", "age", "phone_number", "registration_date", "village", "code", "created_at"])

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

    if "signed_in" not in st.session_state:
        st.session_state.signed_in = False
        if "member_code" not in st.session_state:
            st.session_state.member_code = ""

            menu = st.sidebar.radio("menu", ["register", "sign_in", "members_list"])

df = load_data()

if Menu == "register":
    with st.form("register_form"):
        full_name = st.text_input("full name")
        position = st.text_input("position")
        age = st.number_input("age", min_value=0)
        phone_number = st.text_input("phone number")
        village = st.text_input("village")
        submitted = st.form_submit_button("register")

        if submitted:
            if full_name and position and age and phone_number and village:
                code = str(uuid.uuid4())[:8].upper()
                new_row = pd.DataFrame([[full_name, position, age, phone_number, datetime.now().strtime("%y-%m-%d %h:%M:%S"), village, code, datetime.now().strtime("%Y-%M-%d %H:%M:%S")]], columns=df.columns)
                df = pd.contact([df, new_row], ignore_index=True)
                save_data(df)
                st.success(f"registration successfull! your member code is {code}")
            else:
                st.error("please fill in all the fields to register")
            if Menu == "sign_in":
                code = st.text_input("enter your code to sign in")
                if st.button("sign in"):
                    match = df[df["code"].astype(str) == code.strip().upper()]
                    if not match.empty:
                        st.session_state.signed_in = True
                        st.session_state.member_code = code.strip().upper()
                        st.success(f"sign in as {match.iloc[0]['full_name']}")
                    else:
                        st.error("invalid member code. please try again.")
                        if st.session_state.signed_in:
                            member = df[df["code"] == st.session_state.member_code].iloc[0]
                            if not member.empty:
                                st.info(f"welcome back {member.iloc[0]['full_name']} from{member.iloc[0]['village']}")
                            else:
                                st.subheader("register member")
                                st.dataframe(df, use_container_width=True)
                                
                            
