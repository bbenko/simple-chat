from .base_agent import BaseAgent
import time


class Agent(BaseAgent):
    def respond(self, message):
        # Returns the received message prefixed with 'Server received: '
        time.sleep(0.5)  # Simulate a response time
        return f"Server received: {message}"
