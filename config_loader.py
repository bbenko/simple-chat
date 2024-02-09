import os

def load_configuration():
    config = {
        'debug': os.environ.get('SIMPLE_CHAT_DEBUG', 'False').lower() == 'true',
        'port': int(os.environ.get('SIMPLE_CHAT_PORT', 5000)),
        'agent_name': os.environ.get('SIMPLE_CHAT_AGENT', 'echo'),  # Default to Echo agent
        'logging_enabled': os.environ.get('SIMPLE_CHAT_LOGGING', 'False').lower() == 'true'
    }
    return config
