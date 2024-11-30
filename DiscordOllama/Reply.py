import json
import os
import ollama

def initialize_chat_history():
    if not os.path.exists("chat.txt") or os.path.getsize("chat.txt") == 0:
        with open("chat.txt", "w") as chat_history:
            json.dump([], chat_history)

def load_chat_history():
    try:
        with open("chat.txt", "r") as chat_history:
            return json.load(chat_history)
    except json.JSONDecodeError:
        print("Invalid JSON in chat.txt. Resetting to empty list.")
        with open("chat.txt", "w") as chat_history:
            json.dump([], chat_history)
        return []

def ReplyIt(question):
    history = load_chat_history()
    prompt = {'role': 'user', 'content': question}
    history.append(prompt)
    with open("chat.txt", "w") as chat_history:
        json.dump(history, chat_history)
    response = ollama.chat(model="llama3.2:3b", messages=history)
    answer = response['message']['content']
    history.append(response['message'])
    with open("chat.txt", "w") as chat_history:
        json.dump(history, chat_history)
    return answer

initialize_chat_history()
