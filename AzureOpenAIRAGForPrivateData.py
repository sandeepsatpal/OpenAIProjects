import os
import json
import base64
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME", "DEPLOYMENT_NAME")
search_endpoint = os.getenv("SEARCH_ENDPOINT", "SEARCH_ENDPOINT")
search_key = os.getenv("SEARCH_KEY", "SEARCH_KEY")
search_index = os.getenv("SEARCH_INDEX_NAME", "SEARCH_INDEX_NAME")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "API_KEY")

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
            "content": "You are an AI assistant that helps people find information."
        },
        {
            "role": "user",
            "content": chatinput
        },
        {
            "role": "assistant",
            "content": "Based on the retrieved documents."
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
        stream=False,
        extra_body={
          "data_sources": [{
              "type": "azure_search",
              "parameters": {
                "endpoint": f"{search_endpoint}",
                "index_name": "askorobotindex1106",
                "semantic_configuration": "default",
                "query_type": "simple",
                "fields_mapping": {},
                "in_scope": True,
                #"role_information": "You are an AI assistant that helps people find information.",
                "filter": None,
                "strictness": 3,
                "top_n_documents": 5,
                "authentication": {
                  "type": "api_key",
                  "key": f"{search_key}"
                }
              }
            }]
        }
    )
    chatoutput = json.loads(completion.to_json())
    print(chatoutput["choices"][0]["message"]["content"])

#print(completion.to_json())