import json
from langchain.text_splitter import RecursiveCharacterTextSplitter

def create_jsonl_from_chunks(chunks, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for chunk in chunks:
            entry = {
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Details about webscraping methods and data extraction methods"},
                    {"role": "assistant", "content": f"{chunk}"}
                ]
            }
            f.write(json.dumps(entry) + '\n')


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # characters, not tokens
    chunk_overlap=100
)

long_document_text = open("MyCustomContent.txt").read()

chunks = text_splitter.split_text(long_document_text)

create_jsonl_from_chunks(chunks,"MyCustomContentChunks.jsonl")
