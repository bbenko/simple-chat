import time
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    response = f"Server received: {message}"
    time.sleep(1)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
