import tkinter as tk
from tkinter import ttk, scrolledtext
import random
import datetime

class ChatBot:
    def __init__(self, master):
        self.master = master
        master.title("🤖 Chat Assistant")
        master.geometry("700x800")
        master.configure(bg='#2D2D2D')

        # Create main containers
        self.chat_frame = tk.Frame(master, bg='#2D2D2D')
        self.input_frame = tk.Frame(master, bg='#2D2D2D')
        self.reply_frame = tk.Frame(master, bg='#2D2D2D')

        # Chat history
        self.chat_history = scrolledtext.ScrolledText(
            self.chat_frame,
            wrap=tk.WORD,
            font=('Arial', 12),
            bg='#36393F',
            fg='white',
            state='disabled',
            height=15
        )
        self.chat_history.pack(fill=tk.X, expand=True)

        # Input field
        self.user_input = ttk.Entry(
            self.input_frame,
            width=50,
            font=('Arial', 12)
        )
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        # Send button
        self.send_btn = ttk.Button(
            self.input_frame,
            text="Send",
            command=self.process_input
        )
        self.send_btn.pack(side=tk.RIGHT, padx=5)

        # Reply window
        self.reply_label = tk.Label(
            self.reply_frame,
            text="Bot's Response:",
            font=('Arial', 12),
            bg='#2D2D2D',
            fg='white'
        )
        self.reply_label.pack(fill=tk.X)

        self.reply_message = scrolledtext.ScrolledText(
            self.reply_frame,
            wrap=tk.WORD,
            font=('Arial', 12),
            bg='#36393F',
            fg='white',
            state='disabled',
            height=5
        )
        self.reply_message.pack(fill=tk.X, expand=True)

        # Ask question label
        self.ask_label = tk.Label(
            master,
            text="Ask me anything!",
            font=('Arial', 14),
            bg='#2D2D2D',
            fg='white'
        )
        self.ask_label.pack(fill=tk.X, padx=20, pady=10)

        # Layout
        self.chat_frame.pack(fill=tk.X, padx=20, pady=10)
        self.input_frame.pack(fill=tk.X, padx=20, pady=10)
        self.reply_frame.pack(fill=tk.X, padx=20, pady=10)

        # Bind Enter key
        self.user_input.bind("<Return>", lambda e: self.process_input())

        # Simple responses
        self.responses = {
            'hello': ["Hello!", "Hi there!", "Hey!"],
            'time': [f"Current time: {datetime.datetime.now().strftime('%H:%M')}"],
            'date': [f"Today is {datetime.datetime.now().strftime('%Y-%m-%d')}"],
            'default': ["I'm still learning!", "Could you rephrase that?"]
        }

    def process_input(self):
        user_text = self.user_input.get().strip()
        self.user_input.delete(0, tk.END)
        
        if not user_text:
            return
        
        self.add_message("You", user_text)
        self.master.after(500, lambda: self.generate_response(user_text))

    def generate_response(self, text):
        response = ""
        text = text.lower()
        
        if 'hello' in text or 'hi' in text:
            response = random.choice(self.responses['hello'])
        elif 'time' in text:
            response = random.choice(self.responses['time'])
        elif 'date' in text:
            response = random.choice(self.responses['date'])
        else:
            response = random.choice(self.responses['default'])
            
        self.add_message("Bot", response)
        self.add_reply(response)

    def add_message(self, sender, message):
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_history.configure(state='disabled')
        self.chat_history.yview(tk.END)

    def add_reply(self, message):
        self.reply_message.configure(state='normal')
        self.reply_message.delete('1.0', tk.END)
        self.reply_message.insert(tk.END, message)
        self.reply_message.configure(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    bot = ChatBot(root)
    root.mainloop()