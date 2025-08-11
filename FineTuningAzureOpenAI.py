import os
from openai import AzureOpenAI

endpoint = os.getenv("ENDPOINT_URL", "ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4.1")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "API_KEY")

# Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

training_file_name = 'training_set.jsonl'
validation_file_name = 'validation_set.jsonl'
training_file_id = 'file-d4dda76fcdbf44a990a294a7d7e72b49'
validation_file_id = 'file-a72014afd9ce496f80912607b191d5f1'


response = client.fine_tuning.jobs.create(
    training_file=training_file_id,
    validation_file=validation_file_id,
    model="gpt-4.1-2025-04-14", # Enter base model name. Note that in Azure OpenAI, the model name contains dashes and cannot contain dot/period characters.
    seed = 105  # seed parameter controls reproducibility of the fine-tuning job. If no seed is specified, one will be generated automatically.
)

job_id = response.id

# You can use the job ID to monitor the status of the fine-tuning job.
# The fine-tuning job will take some time to start and complete.

print("Job ID:", response.id)
print("Status:", response.id)
print(response.model_dump_json(indent=2))



# Check the status of fine-tuning model
response = client.fine_tuning.jobs.retrieve('ftjob-b170e0aca2c34ff3a07597e3fd374e30')

print("Job ID:", response.id)
print("Status:", response.status)
print(response.model_dump_json(indent=2))