import tkinter as tk
from tkinter import scrolledtext
import requests

class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Client")

        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.config(state=tk.DISABLED)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(padx=10, pady=10)
        self.entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

    def send_message(self, event=None):
        user_message = self.entry.get()
        if user_message:
            self.display_message("User", user_message)
            self.entry.delete(0, tk.END)
            response = self.send_to_server(user_message)
            self.display_message("Bot", response)

    def send_to_server(self, message):
        try:
            response = requests.post("http://localhost:5000/chat", json={"message": message})
            response_data = response.json()
            return response_data.get("response", "No response from server")
        except Exception as e:
            return f"Error: {e}"

    def display_message(self, sender, message):
        self.chat_area.config(state=tk.NORMAL)
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state=tk.DISABLED)
        self.chat_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()