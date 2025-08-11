from langchain_openai import AzureChatOpenAI
from langchain.schema import HumanMessage
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


# Set your Azure OpenAI credentials
import os
os.environ["AZURE_OPENAI_API_KEY"] = "API_KEY"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://openaiprojects.openai.azure.com/"
os.environ["AZURE_OPENAI_API_VERSION"] = "2025-01-01-preview"  # or the version you're using

# Initialize the AzureChatOpenAI model

chat = AzureChatOpenAI(
    azure_deployment="gpt-4.1",
    azure_endpoint="azure_endpoint",
    api_key="api_key",
    api_version="2025-01-01-preview"
)


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

chain = LLMChain(llm=chat, prompt=prompt)

#result = chain.run(question="What is LangChain?")
#print(result)


# Example usage
response = chat([HumanMessage(content="Which base model you are using?")])
print(response.content)
