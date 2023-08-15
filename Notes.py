import tkinter as tk
import json


class NotesGUI:
    def __init__(self):
        self.notes = []

        # create main window
        self.root = tk.Tk()
        self.root.title("Notes App")

        # create widgets
        title_label = tk.Label(self.root, text="Title:")
        title_label.grid(row=0, column=0, padx=5, pady=5)

        self.title_entry = tk.Entry(self.root, width=50)
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)

        content_label = tk.Label(self.root, text="Content:")
        content_label.grid(row=1, column=0, padx=5, pady=5)

        self.content_text = tk.Text(self.root, width=50, height=10)
        self.content_text.grid(row=1, column=1, padx=5, pady=5)

        add_button = tk.Button(self.root, text="Add Note", command=self.add_note)
        add_button.grid(row=2, column=0, padx=5, pady=5)

        self.notes_list = tk.Listbox(self.root, width=50)
        self.notes_list.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        self.notes_list.bind("<<ListboxSelect>>", self.load_selected_note)

        try:
            with open("notes.json", "r") as f:
                self.notes = json.load(f)
                for note in self.notes:
                    self.notes_list.insert(tk.END, note["title"])
        except FileNotFoundError:
            pass

        # start main loop
        self.root.mainloop()

    def add_note(self):
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END)
        note = {"title": title, "content": content}
        self.notes.append(note)
        self.notes_list.insert(tk.END, title)
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)

    def load_selected_note(self, event):
        index = self.notes_list.curselection()
        if index:
            note = self.notes[index[0]]
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, note["title"])
            self.content_text.delete("1.0", tk.END)
            self.content_text.insert("1.0", note["content"])

    def load_notes(self):
        try:
            with open("notes.txt", "r") as f:
                for line in f:
                    note = eval(line.strip())
                    self.notes.append(note)
                    self.notes_list.insert(tk.END, note["title"])
        except FileNotFoundError:
            pass

    def save_notes(self):
        with open("notes.json", "w") as f:
            json.dump(self.notes, f)

if __name__ == "__main__":
    gui = NotesGUI()
