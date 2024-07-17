import requests
import argparse

# Replace API key with your own key

OLLAMA_API_KEY = 'LL-90TYmcL3kp0XKJUxgBI9j0tf2HdAAaAz7ude7CXAmr0miGYK0SsYpik2nZi0dgFy'
OLLAMA_API_URL = 'https://api.ollama.com/v1/models/qwen2-0.5b/summarize'

def get_summary(text):
    headers = {
        'Authorization': f'Bearer {OLLAMA_API_KEY}',
        'Content-Type': 'application/json'
    }
    payload = {
        'text': text
    }
    response = requests.post(OLLAMA_API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('summary', 'No summary available.')
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    parser = argparse.ArgumentParser(description='Summarize text using the Ollama API and Qwen2 0.5B model.')
    parser.add_argument('--file', type=str, help='Path to the text file to summarize')
    parser.add_argument('--text', type=str, help='Text to summarize')

    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, 'r') as file:
                text = file.read()
        except FileNotFoundError:
            print(f"Error: The file {args.file} was not found.")
            return
    elif args.text:
        text = args.text
    else:
        print("Error: You must provide either a text file (--file) or text (--text) to summarize.")
        return

    summary = get_summary(text)
    print("Summary:")
    print(summary)

if _name_ == '_main_':
    main()
