import os
import time
import google.genai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def call_gemini(prompt: str) -> str:
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text
        except ResourceExhausted as e:
            if attempt < max_retries - 1:
                retry_delay = getattr(e, 'retry_delay', None)
                if retry_delay:
                    if hasattr(retry_delay, 'total_seconds'):
                        wait_time = retry_delay.total_seconds()
                    else:
                        wait_time = retry_delay
                    print(f"Rate limit exceeded. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print("Rate limit exceeded. Retrying in 60 seconds...")
                    time.sleep(60)
            else:
                print("Rate limit exceeded after retries. Returning error message.")
                return "Error: Rate limit exceeded for Gemini API. Please try again later or upgrade your plan."
        except Exception as e:
            print(f"Unexpected error: {e}")
            return f"Error: {str(e)}"
