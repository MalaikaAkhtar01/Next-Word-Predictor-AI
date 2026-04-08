import os
import tkinter as tk
from tkinter import messagebox
import nltk
import re
from collections import defaultdict, Counter

class TrigramModel:
    def __init__(self, alpha=0.01):
        self.alpha = alpha
        self.trigram_counts = defaultdict(Counter)
        self.bigram_counts = defaultdict(int)
        self.vocab = set()

    def clean_text(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text.split()

    def train_incremental(self, sentence):
        """Naye sentence se seekhne wala function"""
        words = self.clean_text(sentence)
        if len(words) < 3:
            return False
        
        self.vocab.update(words)
        for i in range(len(words) - 2):
            w1, w2, w3 = words[i], words[i+1], words[i+2]
            self.trigram_counts[(w1, w2)][w3] += 1
            self.bigram_counts[(w1, w2)] += 1
        return True

    def train_from_directory(self, data_dir, limit=1000):
        print(f"Loading initial data...")
        count = 0
        for label_type in ['pos', 'neg']:
            dir_name = os.path.join(data_dir, label_type)
            if not os.path.exists(dir_name): continue
            for fname in os.listdir(dir_name):
                if count >= limit: break
                if fname.endswith('.txt'):
                    with open(os.path.join(dir_name, fname), encoding='utf-8') as f:
                        self.train_incremental(f.read())
                    count += 1
        self.vocab.add("<UNK>")

    def get_prediction(self, user_input, top_n=3):
        tokens = self.clean_text(user_input)
        if len(tokens) < 2: return []
        w1, w2 = tokens[-2], tokens[-1]
        
        # Check if context exists
        if (w1, w2) not in self.bigram_counts:
            return []

        V = len(self.vocab)
        context_count = self.bigram_counts[(w1, w2)]
        probs = {}
        
        for word, count in self.trigram_counts[(w1, w2)].items():
            probs[word] = (count + self.alpha) / (context_count + self.alpha * V)
        
        sorted_predictions = sorted(probs.items(), key=lambda x: x[1], reverse=True)
        return [word for word, prob in sorted_predictions[:top_n]]

class ModernPredictorGUI:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.root.title("✨ AI Sentence Generator & Learner")
        self.root.geometry("600x550")
        self.root.configure(bg="#2C3E50")

        # Header
        tk.Label(root, text="NLP Trigram Predictor", font=("Segoe UI", 24, "bold"), fg="#ECF0F1", bg="#2C3E50").pack(pady=10)

        # Input Area
        self.text_entry = tk.Entry(root, font=("Consolas", 14), width=40, bg="#34495E", fg="white", insertbackground="white")
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<KeyRelease>", self.on_key_release)

        # Learning Section
        self.learn_btn = tk.Button(root, text="Add to Memory 🧠", command=self.learn_sentence, bg="#1ABC9C", fg="white", font=("Segoe UI", 10, "bold"))
        self.learn_btn.pack(pady=5)

        # Suggestions
        tk.Label(root, text="SUGGESTIONS", font=("Segoe UI", 10, "bold"), fg="#1ABC9C", bg="#2C3E50").pack(pady=5)
        self.btn_frame = tk.Frame(root, bg="#2C3E50")
        self.btn_frame.pack(pady=10)

        self.colors = ["#E74C3C", "#3498DB", "#F1C40F"]
        self.buttons = []
        for i in range(3):
            btn = tk.Button(self.btn_frame, text="---", font=("Segoe UI", 11, "bold"), width=12, bg=self.colors[i], fg="white", command=lambda i=i: self.insert_word(i))
            btn.pack(side=tk.LEFT, padx=10)
            self.buttons.append(btn)

    def learn_sentence(self):
        text = self.text_entry.get()
        if self.model.train_incremental(text):
            messagebox.showinfo("Success", f"Learned: '{text}'")
        else:
            messagebox.showwarning("Short Sentence", "Please type at least 3 words to learn trigrams!")

    def on_key_release(self, event):
        text = self.text_entry.get()
        preds = self.model.get_prediction(text)
        for i in range(3):
            if i < len(preds):
                self.buttons[i].config(text=preds[i], state=tk.NORMAL)
            else:
                self.buttons[i].config(text="---", state=tk.DISABLED)

    def insert_word(self, idx):
        word = self.buttons[idx].cget("text")
        current = self.text_entry.get().strip()
        self.text_entry.delete(0, tk.END)
        self.text_entry.insert(0, current + " " + word + " ")
        self.on_key_release(None)

if __name__ == "__main__":
    my_model = TrigramModel()
    # Pehle dataset se seekho (optional)
    if os.path.exists("./aclImdb/train"):
        my_model.train_from_directory("./aclImdb/train", limit=500)
    
    root = tk.Tk()
    app = ModernPredictorGUI(root, my_model)
    root.mainloop()