import os
import json
import base64
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME", "DEPLOYMENT_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "AZURE_OPENAI_API_KEY")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# IMAGE_PATH = "YOUR_IMAGE_PATH"
# encoded_image = base64.b64encode(open(IMAGE_PATH, 'rb').read()).decode('ascii')

while True:
    chatinput = input("You: ")
    if chatinput == 'exit':
        break

    # Prepare the chat prompt
    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are an AI assistant that helps people find information."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": chatinput
                }
            ]
        }
    ]

    # Include speech result if speech is enabled
    messages = chat_prompt

    # Generate the completion
    completion = client.chat.completions.create(
        model=deployment,
        messages=messages,
        max_tokens=13107,
        temperature=0.7,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
        stream=False
    )
    chatoutput = json.loads(completion.to_json())
    print(chatoutput["choices"][0]["message"]["content"])

#print(completion.to_json())