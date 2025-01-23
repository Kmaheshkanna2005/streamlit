import streamlit as st
def add():
    number_1=st.number_input("Enter the number_1",value=0)
    number_2=st.number_input("Enter the number_2",value=0)
    if st.button("Add"):
        result=number_1 + number_2
        st.success(f"the result of add is:{result}")
if __name__ == "__main__":
    add()
