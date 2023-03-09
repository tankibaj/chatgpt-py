# ChatGPT-Py

A simple Python script that allows users to interact with the OpenAI GPT API and remembers the conversation history.

![](images/screenshot.png)


This script uses the OpenAI API to generate responses to user prompts and keeps track of the conversation history in a list. When the user inputs `history`, the script prints the entire conversation history. The script uses the OpenAI API key stored in the `OPENAI_API_KEY` environment variable, so make sure to set this variable to your API key before running the script.

```bash
export OPENAI_API_KEY=<you api key>
```

```bash
python3 chatgpt.py
```