# from flask import Flask, jsonify
# from flask import request
# import random

# app = Flask(__name__)

# @app.route('/get_numbers', methods=['GET'])
# def get_numbers():
#     # Generate 5 random numbers
#     count = request.args.get('count', default=5, type=int)
#     numbers = [random.randint(1, 100) for _ in range(count)]
#     # print(numbers)
#     return jsonify({"numbers": numbers})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
#     # get_numbers()