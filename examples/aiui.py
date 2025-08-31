import datetime
import socket
import streamlit as st 

def main():
    script_run_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    host_detail = socket.gethostname()
    st.title("A Streamlit Application")
    st.title("To find out a number square value..")

    # Show runtime info
    st.write(f"Script runs at: {script_run_at}")
    st.write(f"Running on: {host_detail}")
    print("")
    
    # Slider with discrete options and default value 6
    select_number = st.slider("Select a number from this list: ", 0, 100 )

    result = select_number ** 2
    st.write(f"The square of {select_number} is {result}")

if __name__ == "__main__":
    main()
