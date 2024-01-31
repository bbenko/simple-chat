import time
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    response = get_response(message)
    return jsonify({"response": response})


def get_response(message):
    time.sleep(1)  # make it look like the server is doing something
    response = f"Server received: {message}" # just echo the message back
    return response


if __name__ == '__main__':
    app.run(debug=True)
