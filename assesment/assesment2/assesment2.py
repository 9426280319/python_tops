import tkinter as tk
from tkinter import messagebox
import os

class Post:
    def __init__(self, username, title, content):
        self.username = username
        self.title = title
        self.content = content

    def save(self):
        filename = f"{self.username}_{self.title}.txt"
        with open(filename, "w") as f:
            f.write(f"User: {self.username}\nTitle: {self.title}\n\n{self.content}")

class MiniBlog:
    def __init__(self, root):
        self.root = root
        self.root.title("MiniBlog")

        tk.Label(root, text="Username").pack()
        self.username = tk.Entry(root)
        self.username.pack()

        tk.Label(root, text="Title").pack()
        self.title = tk.Entry(root)
        self.title.pack()

        tk.Label(root, text="Content").pack()
        self.content = tk.Text(root, height=5)
        self.content.pack()

        tk.Button(root, text="Save Post", command=self.save_post).pack()

        self.listbox = tk.Listbox(root)
        self.listbox.pack()
        self.listbox.bind("<<ListboxSelect>>", self.view_post)

        self.display = tk.Text(root, height=10)
        self.display.pack()

        self.load_posts()

    def save_post(self):
        username = self.username.get()
        title = self.title.get()
        content = self.content.get("1.0", tk.END)

        if not username or not title or not content.strip():
            messagebox.showerror("Error", "All fields required")
            return

        try:
            post = Post(username, title, content)
            post.save()
            messagebox.showinfo("Success", "Post saved")
            self.load_posts()
        except:
            messagebox.showerror("Error", "Failed to save")

    def load_posts(self):
        self.listbox.delete(0, tk.END)
        for file in os.listdir():
            if file.endswith(".txt"):
                self.listbox.insert(tk.END, file)

    def view_post(self, event):
        try:
            file = self.listbox.get(self.listbox.curselection())
            with open(file, "r") as f:
                data = f.read()
            self.display.delete("1.0", tk.END)
            self.display.insert(tk.END, data)
        except:
            messagebox.showerror("Error", "Cannot open file")

root = tk.Tk()
app = MiniBlog(root)
root.mainloop()