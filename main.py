import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    if len(sys.argv) < 2 :
        print("Usage: python3 script.py <prompt> [--verbose]")
        sys.exit(1)

    user_prompt = sys.argv[1]

    verbose = False
    if len(sys.argv) > 2 and sys.argv[2] == '--verbose':
        verbose = True
    elif '--verbose' in sys.argv:
        verbose = True
    
    if verbose:
        print(f'User prompt: {user_prompt}')


    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')

    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables")
        sys.exit(1)


    try:
        client = genai.Client(api_key=api_key)

        messages = [
            types.Content(role='user', parts=[types.Part(text = user_prompt)])
        ]
        
        generate_content(client, messages, verbose)
    except Exception as e:
        print(f"Error initializing client or generating content: {e}")
        sys.exit(1)
    

def generate_content(client, messages, verbose):
    system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt)
            )
        
        if verbose:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}",
                      )
        
        print(f"Response:\n{response.text}")
    except Exception as e:
        print(f"Error generating content: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()