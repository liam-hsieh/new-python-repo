import streamlit as st
# it will work if the repo is installed as a package by uv
from example_module2 import import_checking2

st.set_page_config(page_title="Demo App", layout="wide")

st.title("Demo Streamlit App")
st.write("Testing import_checking2 from example_module2")

# Input section
st.subheader("Input")
user_input = st.text_input("Enter something to check:")

# Process with import_checking2
if user_input:
    st.subheader("Result")
    result = import_checking2(user_input)
    st.write(result)
else:
    st.info("Enter text above to see results")

# Footer
st.divider()
st.caption("Powered by Streamlit")