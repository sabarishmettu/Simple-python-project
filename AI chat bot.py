import tkinter as tk
import openai

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"

def send_message():
    # Get user input from text box
    message = entry.get()
    # Clear text box
    entry.delete(0, tk.END)
    # Add user input to chat log
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + message + "\n")
    chat_log.config(state=tk.DISABLED)
    # Use OpenAI API to generate response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='You: ' + message + '\nAI:',
        max_tokens=2048,
        temperature=0.5
    )
    # Add response to chat log
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "AI: " + response["choices"][0]["text"] + "\n")
    chat_log.config(state=tk.DISABLED)
    # Scroll to bottom of chat log
    chat_log.yview(tk.END)

# Set up tkinter GUI
root = tk.Tk()
root.title("Chatbox")

# Create chat log
chat_log = tk.Text(root)
chat_log.config(state=tk.DISABLED)
chat_log.pack()

# Create text entry box
entry = tk.Entry(root)
entry.pack()

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
