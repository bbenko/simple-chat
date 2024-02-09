import os
from openai import OpenAI
from .base_agent import BaseAgent

class Agent(BaseAgent):
    """
    This class represents an agent that interacts with the any LLM compatible with OpenAI API. Tested with OpenAI and Together AI.
    Set the following environment variables:
    - LLM_API_KEY: The API key for accessing the OpenAI API or Together AI.
    - LLM_BASE_URL: The base URL for the OpenAI API or Together AI. 'https://api.together.xyz/v1' for Together AI and 'https://api.openai.com/v1' for OpenAI.
    - LLM_MODEL: The name or ID of the chat model to use. Check https://docs.together.ai/docs/inference-models or https://platform.openai.com/docs/api-reference/models/list.
                 For example, "gpt-3.5-turbo", 'mistralai/Mistral-7B-Instruct-v0.1', 'mistralai/Mixtral-8x7B-Instruct-v0.1', 'meta-llama/Llama-2-70b-chat-hf', ...
    - LLM_TEMPERATURE: The temperature parameter for generating responses.
    - LLM_MAX_TOKENS: The maximum number of tokens in the generated response.
    - LLM_TOP_P: The top-p parameter for generating responses.
    - LLM_SYSTEM_MESSAGE: The system message to be included in the chat. This are instructions for the AI to follow.
    """

    def __init__(self):
        """
        Initializes the Agent object.

        Parameters:
        - api_key (str): The API key for accessing the OpenAI API.
        - model (str): The name or ID of the chat model to use. For example, "gpt-3.5-turbo".
        - temperature (float): The temperature parameter for generating responses.
        - max_tokens (int): The maximum number of tokens in the generated response.
        - top_p (float): The top-p parameter for generating responses.
        - system_message (str): The system message to be included in the chat.
        - base_url (str): The base URL for the OpenAI API.
        """
        self.api_key = os.environ.get('LLM_API_KEY', '')
        self.base_url = os.environ.get('LLM_BASE_URL', 'https://api.together.xyz/v1')
        self.model = os.environ.get('LLM_MODEL', 'mistralai/Mistral-7B-Instruct-v0.1')        
        self.temperature = float(os.environ.get('LLM_TEMPERATURE', 0.7))
        self.max_tokens = int(os.environ.get('LLM_MAX_TOKENS', 512))
        self.top_p = float(os.environ.get('LLM_TOP_P', 0.7))
        self.system_message = os.environ.get('LLL_SYSTEM_MESSAGE', 'You are a helpful assistant.')
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)
        
    def respond(self, message):
        try:
            chat_completion = self.client.chat.completions.create(
                model=self.model, 
                temperature=self.temperature, 
                max_tokens=self.max_tokens, 
                top_p=self.top_p, 
                messages=[
                    {
                        "role": "system",
                        "content": self.system_message
                    },
                    {
                        "role": "user",
                        "content": message
                    },
                ]
            )
            response = chat_completion.choices[0].message.content
            return response
        except Exception as e:
            print(f"An error occurred: {e}")
            return e.__str__()
