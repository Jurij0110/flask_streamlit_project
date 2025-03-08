import streamlit as st
import requests

# Title of the Streamlit app
st.title("Random Number Generator")

# Instructions
st.write("Click the button below to fetch random numbers from the Flask API.")

count = st.slider("How many numbers?", 1, 20, 5)
# Button to fetch numbers
if st.button("Get Random Numbers"):
    try:
        # Call the Flask API
        
        response = requests.get(f"http://localhost:5000/get_numbers?count={count}")
        # print((response))
        st.write(f"Here is the count: {count}")
        data = response.json()
        
        # Display the numbers
        st.write("Here are your random numbers:")
        st.json(data["numbers"])
    except Exception as e:
        st.error(f"Error fetching numbers: {e}")


    
# Run instructions
st.write("Note: Make sure the Flask API (api.py) is running in another terminal!")