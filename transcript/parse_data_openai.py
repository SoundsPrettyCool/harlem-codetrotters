from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPEN_ROUTER_API_KEY')

def extract_topics(paragraph):
    """
    Takes a paragraph and returns the topics discussed in it.
    
    Args:
        paragraph (str): The input paragraph to analyze
        
    Returns:
        str: The topics extracted from the paragraph
    """
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",
            "X-Title": "<YOUR_SITE_NAME>",
        },
        extra_body={},
        model="openai/gpt-4-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Extract the main topics from this paragraph:\n\n{paragraph}"
            }
        ]
    )
    
    return completion.choices[0].message.content

print(extract_topics("the subject of this sentence is artificial intelligence and machine learning."))