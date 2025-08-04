import streamlit as st

# streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square , cube and fifth power")

#get user input
n = st.number_input("Enter a number", value=1 , step=1)

#calculatio
if st.button("Calculate"):
    square = n ** 2
    cube = n ** 3
    fifth = n ** 5

# display results
st.write(f"Square of {n} is : {square}")
st.write(f"Cube of {n} is : {cube}")
st.write(f"Fifth power of {n} is : {fifth}")