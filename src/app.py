import streamlit as st
from pathlib import Path
from generator import generate_profile

st.title(":school_satchel: Github Profile Generator")

# Personal information
st.header("Personal Information")
with st.expander("Personal Information"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Name")
    email = col2.text_input("Email")
    location = st.text_input("Location")
    phone = col1.text_input("Phone Number")
    website = col2.text_input("Website")

# Social media
st.header("Social Media")
with st.expander("Social Media"):
    st.markdown("Enter your social media username(not links):")
    col1, col2 = st.columns(2)
    twitter = col2.text_input("Twitter")
    linkedin = col1.text_input("LinkedIn")
    github = col1.text_input("GitHub")
    instagram = col2.text_input("Instagram")

# Select themes
st.header("Select Theme")
themes = list(map(lambda x: x.stem, Path("src/themes").iterdir()))
theme = st.selectbox("Select Theme", themes)
st.markdown(f"Select Theme: **{theme}**")

# Generate README
st.header("Generate README")
if st.button("Generate README"):
    st.markdown("Generating README...")
    profile = generate_profile(
        theme=theme,
        name=name,
        email=email,
        location=location,
        phone=phone,
        website=website,
        twitter=twitter,
        linkedin=linkedin,
        github=github,
        instagram=instagram,
    )
    st.code(profile)
