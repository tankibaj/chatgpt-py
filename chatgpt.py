import requests
import os

# Set up OpenAI API credentials
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# Define conversation history list
conversation_history = []


# Define function to send user prompt to OpenAI GPT API and return response
def get_openai_response(prompt):
    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": 500,
        "temperature": 0.5
    }
    try:
        response = requests.post("https://api.openai.com/v1/completions", json=data, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["text"].strip()
    except Exception as e:
        print("OpenAI API request failed: ", e)
        print("HTTP response:", response.content if response else "")
        return ""


# Define function to add user input and OpenAI GPT response to conversation history list
def add_to_history(user_input, openai_response):
    conversation_history.append(f"\033[38;5;250mYou: {user_input}\033[0m")
    conversation_history.append(f"\033[32mChatGPT: {openai_response}\033[0m")


# Define function to print conversation history
def print_history():
    print("\n".join(conversation_history))


# Start conversation loop
while True:
    # Get user input
    user_input = input("\033[38;5;250mYou:\033[0m ")

    # If user input is "history", print conversation history
    if user_input == "history":
        print_history()
        continue

    # Send user input to OpenAI GPT API and get response
    prompt = "\n".join(conversation_history) + f"\nYou: {user_input}\nChatGPT:"
    openai_response = get_openai_response(prompt)

    # Print OpenAI GPT response
    if openai_response:
        print(f"\033[32mChatGPT:\033[0m {openai_response}")
    else:
        print("\033[32mChatGPT:\033[0m Sorry, I didn't understand. Could you please rephrase?")

    # Add user input and OpenAI GPT response to conversation history list
    add_to_history(user_input, openai_response)
