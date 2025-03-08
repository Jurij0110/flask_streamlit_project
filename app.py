# import streamlit as st
# import requests

# # Title of the Streamlit app
# st.title("Random Number Generator")

# # Instructions
# st.write("Click the button below to fetch random numbers from the Flask API.")

# count = st.slider("How many numbers?", 1, 20, 5)
# # Button to fetch numbers
# if st.button("Get Random Numbers"):
#     try:
#         # Call the Flask API
        
#         response = requests.get(f"http://localhost:5000/get_numbers?count={count}")
#         # print((response))
#         st.write(f"Here is the count: {count}")
#         data = response.json()
        
#         # Display the numbers
#         st.write("Here are your random numbers:")
#         st.json(data["numbers"])
#     except Exception as e:
#         st.error(f"Error fetching numbers: {e}")


    
# # Run instructions
# st.write("Note: Make sure the Flask API (api.py) is running in another terminal!")


import streamlit as st
from flask import Flask, jsonify, request
import random
import threading
import requests
import time

# Flask app
flask_app = Flask(__name__)

@flask_app.route('/get_numbers', methods=['GET'])
def get_numbers():
    count = request.args.get('count', default=3, type=int)
    numbers = [random.randint(1, 100) for _ in range(count)]
    return jsonify({"numbers": numbers})

# Function to run Flask in a thread
def run_flask():
    flask_app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

# Start Flask in a background thread
threading.Thread(target=run_flask, daemon=True).start()

# Give Flask a moment to start
time.sleep(2)

# Streamlit app
st.title("Random Number Generator")
st.write("Click the button below to fetch random numbers from the internal Flask API.")

# Slider for number count
count = st.slider("How many numbers?", 1, 10, 3)  # Min: 1, Max: 10, Default: 3
if st.button("Get Random Numbers"):
    try:
        response = requests.get(f"http://localhost:5000/get_numbers?count={count}")
        data = response.json()
        st.write("Here are your random numbers:")
        st.json(data["numbers"])
    except Exception as e:
        st.error(f"Error fetching numbers: {e}")