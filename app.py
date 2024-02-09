import logging
from flask import Flask, request, jsonify, render_template
from config_loader import load_configuration  # Import the configuration loader
from agent_loader import load_agent  # Import the agent loader

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

app = Flask(__name__)
app.simple_chat_config = load_configuration()  # Load configuration
app.simple_chat_agent = load_agent(app.simple_chat_config)  # Load agent

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    if app.simple_chat_config['logging_enabled']:
        logging.info(f"Received message: {message}")

    response = app.simple_chat_agent.respond(message)
    if app.simple_chat_config['logging_enabled']:
        logging.info(f"Responded with: {response}")

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=app.simple_chat_config['port'], debug=app.simple_chat_config['debug'])
